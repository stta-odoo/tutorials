from odoo import api, fields, models
from odoo.exceptions import UserError

class Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer"
    _order = "price desc"
    price = fields.Float()
    status = fields.Selection([("accepted","Accepted"), ("refused","Refused")], 
                             copy=False)
    buyer_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'An offer price must be strictly positive'),
    ]
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Date.today(), days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                if record.create_date:
                    record.validity = (record.date_deadline - record.create_date.date()).days
                else:
                    record.validity = (record.date_deadline - fields.Date.today()).days
    
    def action_accept(self):
        for record in self:
            if record.property_id.buyer_id:
                raise UserError(("Only 1 offer can be Accepted."))
                return True
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.buyer_id
            # 1. when it's triggered, we should know if there is offer accepted -> raise error if there is
        return True
    
    def action_refuse(self):
        for record in self:
            if record.status == "accepted":
                record.property_id.selling_price = 0
                record.property_id.buyer_id = False
            record.status = "refused"
        return True
    
    def action_cancel(self):
        for record in self:
            if record.status == "accepted":
                record.property_id.selling_price = 0
                record.property_id.buyer_id = False
            record.status = ""
        return True