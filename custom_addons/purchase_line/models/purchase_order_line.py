# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    team_lead_ids = fields.One2many("account.move.line", "partner_id")
    order_line = fields.Char(string="Order Line", store=True)
