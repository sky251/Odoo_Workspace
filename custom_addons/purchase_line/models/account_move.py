from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    order = fields.Char(related="member_id.order_line", string="Order")

    partner_id = fields.Many2one("purchase.order.line", string="zzz")
    member_id = fields.Many2one("purchase.order.line", string="Member")
