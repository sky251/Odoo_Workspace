# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class Product(http.Controller):
    @http.route("/products", type="http", website=True, auth="user", csrf=False)
    def product(self, **kw):
        products = (
            request.env["product.template"].sudo().search([("sale_ok", "=", True)])
        )
        return request.render(
            "sale_commision.product_template_view", {"products": products}
        )

    @http.route("/product_update", type="http", website=True, auth="user", csrf=False)
    def product_update(self, **kw):
        return request.render("sale_commision.product_update_template_view")
