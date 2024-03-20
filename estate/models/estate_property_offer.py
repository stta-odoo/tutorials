from odoo import fields, models

class Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Property offer"
    price = fields.Float()
    status = fields.Selection([("accepted","Accepted"), ("refused","Refused")], 
                             copy=False)
    buyer_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)