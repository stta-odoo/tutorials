from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_utils

class Property(models.Model):

    _name = "estate.property"
    _description = "Properties of an estate"
    _order = "id desc"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From", copy=False, default=fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [("north", "North"),("west", "West"),("east","East"),("south","South")]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection = [("new","New"), ("offer_received","Offer Received"), ("offer_cccepted","Offer Accepted"), ("sold","Sold"), ("canceled","Canceled")],
        required = True,
        default = "new",
        copy = False,
        string = "Status",
    )

    property_type_id = fields.Many2one("estate.property.type", 
                                       string="Property Type",
                                       )
    
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False, readonly=True)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'Selling price must not be negative.'),
        ('check_expected_price', 'CHECK(expected_price > 0)', 'Expected price must not be negative.'),
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price")) if record.offer_ids else 0
        
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_sold_click(self):
        for record in self:
            if record.state == "canceled":
                raise UserError(("Sold property cannot be canceled."))
            record.state = "sold"
        return True
    
    def action_cancel_click(self):
        for record in self:
            if record.state == "sold":
                raise UserError(("Canceled property cannot be sold."))
            record.state = "canceled"
        return True

    @api.constrains("selling_price", "expected_price")
    def _check_selling_price(self):
        _precision_rounding = self.env["decimal.precision"].precision_get("Account")
        for record in self:
            if not float_utils.float_is_zero(record.selling_price, _precision_rounding) and float_utils.float_compare(record.selling_price, 0.9*record.expected_price, _precision_rounding) == -1:
                raise ValidationError("Selling price cannot be lower than 0.9x of the expected price") 