from odoo import fields, models

class Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tag"
    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'A property tag name and property type name must be unique'),
    ]