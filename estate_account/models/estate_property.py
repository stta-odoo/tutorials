from odoo import models

class Property(models.Model):
    _inherit = "estate.property"

    def action_sold_click(self):
        return super().action_sold_click()