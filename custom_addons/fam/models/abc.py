from odoo import models, fields


class PracticeAbc(models.Model):
    _inherit = "sale.order"

    practice = fields.Char(string="Practice")
