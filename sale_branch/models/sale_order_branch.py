from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrderBranch(models.Model):
    _name = "sale.order.branch"
    name = fields.Char(required=True)
    sequence_id = fields.Many2one("ir.sequence", string="Sequence")

    _sql_constraints = [
        ('unique_sale_order_branch_name', 'UNIQUE(name)', 'A branch name must be unique'),
    ]

    @api.model_create_multi
    def create(self, val_list):
        for val in val_list: 
            sequence_id =  self.env['ir.sequence'].search([("name", "=", val["name"])], limit=1).id or self.env['ir.sequence'].create([{"name": val["name"]}]).id
            val["sequence_id"] = sequence_id
        return super().create(val_list)