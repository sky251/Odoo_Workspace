from odoo import fields, models
from odoo.tools.translate import _

# from .product import ProductProduct


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_capacity = fields.Float(string=_("Total Capacity"), readonly=True)

    def total_cap_on_button_click(self):
        for order in self:
            total_capacity = 0
            for line in order.order_line:
                total_capacity += line.max_qty_allowed
            order.update({"total_capacity": total_capacity})


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    max_qty_allowed = fields.Float(
        related="product_id.qty_on_order", string=_("Max Qty Allowed")
    )
