from odoo import Command, models
from odoo.tools import float_utils

class Property(models.Model):
    _inherit = "estate.property"

    def action_sold_click(self):
        # self._create_invoice(self)
        _precision = self.env["decimal.precision"].precision_get("Account")
        journal = self.env["account.journal"].search([
                *self.env["account.journal"]._check_company_domain(self.env.company),
                ("type", "=", "sale"),
            ], limit=1)
        
        vals = {
            "move_type": "out_invoice",
            "partner_id": self.buyer_id.id,
            "journal_id": journal.id,
            "invoice_line_ids": [Command.create({
                "name":"Down Payment", 
                "quantity":1,
                "price_unit": float_utils.float_round(0.06*self.best_price, precision_digits=_precision),
            }),Command.create({
                "name":"Administrative Fee", 
                "quantity":1,
                "price_unit": 100,
            })]
        }
        self.env["account.move"].create(vals)

        return super().action_sold_click()
