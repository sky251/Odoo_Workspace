from collections import OrderedDict
from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.http import request, route


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['site_count'] = request.env['construction.site'].sudo().search_count([])
        return values

    @http.route("/my/check_construction_site", type="http", website=True, auth="user", csrf=False)
    def check_construction_site(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        Sites = request.env["construction.site"]

        domain = []

        searchbar_sortings = {
            'name': {'label': 'Name', 'order': 'name asc'},
            'scheduled_date': {'label': 'Date', 'order': 'scheduled_date asc'},
        }
        # default sort by value
        if not sortby:
            sortby = 'name'
        order = searchbar_sortings[sortby]['order']

        searchbar_filters = {
            'all': {'label': 'All', 'domain': []},
            'draft': {'label': 'Draft', 'domain': [('state', '=', 'draft')]},
        }
        # default filter by value
        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']

        # count for pager
        site_count = Sites.search_count(domain)
        # make pager
        pager = portal_pager(
            url="/my/check_construction_site",
            url_args={'sortby': sortby, 'filterby': filterby},
            total=site_count,
            page=page,
            step=self._items_per_page
        )
        site = Sites.search(domain,order=order,limit=self._items_per_page,offset=pager['offset'])

        values.update({
            'sites': site,
            'page_name': 'const_site',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            'default_url': '/my/check_construction_site',
        })

        return request.render("construction_site.portal_my_construction_site", values)

    @http.route("/my/check_construction_site/<int:site.id>", type="http", website=True, auth="user", csrf=False)
    def my_check_construction_site(self,site,**kw):
        print("\n\n\n\n\n ajdsnvfkbasbdcvlb ==========")
