from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _compute_total_amount(self):
        subtotal = 0
        for order in self.env["sale.order"].search([("partner_id", "=", self.id)]):
            subtotal = subtotal + order.amount_total
        self.total_amount = subtotal
    # def _compute_total_amount(self):
    #     subtotal = 0
    #     for order in self.env["sale.order"].search([("partner_id", "=", self.id)]):
    #         for line in order.order_line:
    #             subtotal = subtotal + line.price_subtotal
    #     self.total_amount = subtotal

    total_amount = fields.Integer(string="Total Amount", compute=_compute_total_amount)
    def open_tree_view(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Order Line",
            # "view_type":"tree,form",
            # "view_mode": "tree,form",
            'views': [[self.env.ref('sale.view_order_line_tree').id, 'tree'], [self.env.ref('sale.sale_order_line_view_form_readonly').id, 'form']],
            "res_model": "sale.order.line",
            "domain": [("order_partner_id.id", "=", self.id)],
        }
