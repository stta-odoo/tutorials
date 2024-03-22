from odoo import api, fields, models

class Property_Type(models.Model):
    _name = "estate.property.type"
    _description = "Property type"
    _order = "sequence, name"
    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many(related="property_ids.offer_ids")
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = 0
            for property in self.property_ids:
                record.offer_count += len(property.offer_ids)
    