from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    commision_value = fields.Float(string="Sales Commission", default=2.5)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("order_id.commision_value", "price_subtotal")
    def _compute_product_commission(self):
        print("\n\n\n\n\n _compute_product_commission: ",self)
        for line in self:
            line.production_commission = line.price_subtotal * (
                line.order_id.commision_value / 100
            )

    production_commission = fields.Float(
        string="Production commission", compute=_compute_product_commission, store=True
    )
