from odoo import fields, models

class Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property type"
    _order = "sequence, name"
    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    property_ids = fields.One2many("estate.property", "property_type_id")
    