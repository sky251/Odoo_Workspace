from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    sssss = fields.Boolean(string="Bool")
