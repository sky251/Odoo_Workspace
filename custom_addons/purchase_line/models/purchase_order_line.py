# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    order_line_cus = fields.Char(string="Order Line", store=True)

    def _prepare_account_move_line(self):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line()
        res.update(
            {
                "order_line_cus": self.order_line_cus,
            }
        )
        return res

    # team_lead_ids = fields.One2many("account.move.line", "partner_id")
    # order_line = fields.Char(string="Order Line", store=True)
