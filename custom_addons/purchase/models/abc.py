from odoo import fields, models


class PracticeAbc(models.Model):
    _inherit = "sale.order"

    practice = fields.Char(string="Practice")
