import json
from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/school", type="http", website=True, auth="public")
    def school_details(self):
        school_data = request.env["res.partner"].search([])
        return request.render(
            "school.school_details_page", {"school_data": school_data}
        )
