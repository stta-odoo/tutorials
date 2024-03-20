from odoo import fields, models

class Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tag"
    name = fields.Char(required=True)