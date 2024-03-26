from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    branch_id = fields.Many2one("sale.order.branch")
    branch_sequence = fields.Char(readonly=True)
    
    def action_confirm(self):
        if self.branch_id:
            self.branch_sequence = self.env['ir.sequence'].next_by_code(self.branch_id.sequence_id.code)
        return super().action_confirm()
    
    # to be tested v
    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        values.update({'branch_sequence': self.branch_sequence})
        return values
    