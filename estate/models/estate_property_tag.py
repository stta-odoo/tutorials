from odoo import fields, models

class Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tag"
    _order = "name"
    name = fields.Char(required=True)
    color = fields.Integer()
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'A property tag name and property type name must be unique'),
    ]