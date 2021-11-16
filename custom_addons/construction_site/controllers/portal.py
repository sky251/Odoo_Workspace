from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.http import request, route
from odoo import http


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['site_count'] = request.env['construction.site'].sudo().search_count([])
        return values


    @http.route("/my/check_construction_site", type="http", website=True, auth="user", csrf=False)
    def check_construction_site(self, **kw):
        sites = request.env["construction.site"].sudo().search([])
        print("\n\n\n\n\n\n\n  Sitessssssss",sites)
        return request.render("construction_site.portal_my_construction_site", {"sites": sites})