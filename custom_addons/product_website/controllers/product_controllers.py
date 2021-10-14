import json

from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/product/", type="http", website=True, auth="public")
    def product_details(self):
        print("\n\n\n\n\n\n Hello this is Product page\n\n\n\n\n\n")
        product_data = request.env["product.template"].search([])
        return request.render(
            "product_website.product_detail_list", {"product_data": product_data}
        )


class ButtonController(http.Controller):
    @http.route(
        "/product/prod/<model('product.template'):product>/",
        type="http",
        website=True,
        auth="public",
    )
    def button_click(self, product):
        print("\n\n\n\n\n\n click on button \n\n\n\n\n\n")
        print("\n\n\n\n\n\n button id \n\n\n\n\n\n", product)
        return request.render(
            "product_website.product_descriptions_page",
            {"product_description": product},
        )
