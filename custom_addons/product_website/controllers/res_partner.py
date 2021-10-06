import json
from odoo import http
from odoo.http import request, route


class ContactController(http.Controller):
    @http.route("/contact/", type="http", website=True, auth="public")
    def contact_details(self):
        print("\n\n\n\n\n\n This is Contact page\n\n\n\n\n\n")
        contacts = request.env["res.partner"].sudo().search([])
        return request.render("product_website.contacts_list", {"contacts": contacts})


    @http.route("/contact/<model('res.partner'):partner>/", type="http", website=True, auth="public")
    def button_click(self, partner):
        print("\n\n\n\n\n\n click Res Contact on button \n\n\n\n\n\n")
        return request.render("product_website.contacts_form_views",{"partner":partner})

