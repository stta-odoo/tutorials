from odoo import api, fields, models

class Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer"
    price = fields.Float()
    status = fields.Selection([("accepted","Accepted"), ("refused","Refused")], 
                             copy=False)
    buyer_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

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
