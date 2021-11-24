from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    order_line_cus = fields.Char(string="Order Line")

    # partner_id = fields.Many2one("purchase.order.line", string="zzz")
    # member_id = fields.Many2one("purchase.order.line", string="Member")
