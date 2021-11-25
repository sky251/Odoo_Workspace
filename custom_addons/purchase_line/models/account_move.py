from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    order_line_cus = fields.Char(string="Order Line")

