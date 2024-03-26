from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    branch_sequence = fields.Char(readonly=True)