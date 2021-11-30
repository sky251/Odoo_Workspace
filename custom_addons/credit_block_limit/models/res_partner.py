from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Boolean(string="Credit Limit", default=False)
    blocking_limit = fields.Boolean(string="Blocking Limit", default=False)
    credit_limit_score = fields.Float(string="Credit Limit Score")
    blocking_limit_score = fields.Float(string="Blocking Limit Score")

