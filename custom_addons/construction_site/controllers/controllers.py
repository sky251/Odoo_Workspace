from odoo import http
from odoo.http import request, route
# import json
# import base64


class CreateEmployees(http.Controller):
    @http.route("/create_employees", type="http", website=True, auth="user", csrf=False)
    def demo_page(self, **kw):
        return request.render("construction_site.craete_employees_template")