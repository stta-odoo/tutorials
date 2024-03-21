from odoo import fields, models

class Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property type"
    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")
    