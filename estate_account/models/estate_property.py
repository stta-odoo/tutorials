from odoo import Command, models
from odoo.exceptions import UserError

class Property(models.Model):
    _inherit = "estate.property"

    def action_sold_click(self):
        # self._create_invoice(self)
        journal = self.env["account.journal"].search([
                *self.env["account.journal"]._check_company_domain(self.env.company),
                ("type", "=", "sale"),
            ], limit=1)
        
        vals = {
            "move_type": "out_invoice",
            "partner_id": self.buyer_id.id,
            "journal_id": journal.id,
        }
        self.env["account.move"].create(vals)

        return super().action_sold_click()
    
    # def _create_invoice(self):
