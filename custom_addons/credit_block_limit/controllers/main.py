from odoo import http
from odoo.http import request, route


class PartnerInfo(http.Controller):
    @http.route("/partner_information", type="http", website=True, auth="user", csrf=False)
    def partner_details(self, **kw):
        members = request.env["res.partner"].sudo().search([])
        values = {"partners": members, 'submit': False}
        if kw:
            states = request.env["res.country.state"].sudo().search([])
            countries = request.env["res.country"].sudo().search([])
            jp, partner = False, False
            if kw.get('partner_id'):
                jp = kw.get('partner_id')
                print("\n\n\n\n\n",jp)
                partner = request.env["res.partner"].sudo().browse(jp)
            values.update({'submit': True, 'partner': partner, 'jp': jp, "countries": countries,"states": states})
        print("\n\n\n\n vals",values)
        return request.render("credit_block_limit.partner_details_template_view",values)
