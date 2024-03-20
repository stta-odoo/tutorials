from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Properties of an estate"
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
    )

    # customer - many2one
    # agent - many2one
    # property type - m2o
    # list of tags - m2m
    # list of offers received - o2m
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    property_tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")