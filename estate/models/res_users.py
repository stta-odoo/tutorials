from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many("estate.property", 
                                   "salesperson_id", 
                                   string="Property",)
    
                                #    domain=['|',('property_ids.state','=','offer_received'),('property_ids.state','=','new')]