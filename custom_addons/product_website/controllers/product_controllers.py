import json
from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/product", type="http", website=True, auth="public")
    def product_details(self):
        print("\n\n\n\n\n\n Hello this is Product page\n\n\n\n\n\n")
        product_data = request.env["product.template"].search([])
        return request.render(
            "product_website.product_detail_list", {"product_data": product_data}
        )
