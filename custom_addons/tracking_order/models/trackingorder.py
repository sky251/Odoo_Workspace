from odoo import api, fields, models


class TrackingOrder(models.Model):
    _name = "tracking.order"

    user_name_id = fields.Many2one("res.users", string="User Name")
    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
