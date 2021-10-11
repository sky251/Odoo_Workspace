import json
from odoo import http
from odoo.http import request, route


class ContactController(http.Controller):
    @http.route("/contact/", type="http", website=True, auth="public")
    def contact_details(self,**kw):
        if kw:
            print("\n\n\n\n\n\n This is Contact page\n\n\n\n\n\n")
            print("\n\n\n\n\n\n   =======>>>>>",kw)
            # contacts = request.env["res.partner"].sudo().search([])

            vals = {
                'name': kw.get('name'),
                'email': kw.get('email'),
                'phone': kw.get('phone'),
            }

            print("=============vals==============", vals)
            request.env["res.partner"].sudo().create(vals)
        else:
            contacts = request.env["res.partner"].sudo().search([])
            return request.render("product_website.contacts_list", {"contacts": contacts})

    @http.route("/contact/<model('res.partner'):partner>/", type="http", website=True, auth="public")
    def button_click(self, partner):
        print("\n\n\n\n\n\n click Res Contact on button \n\n\n\n\n\n")
        return request.render("product_website.contacts_form_views", {"partner": partner})


    @http.route("/contact/create_new_contact/", type="http", website=True, auth="public")
    def create_new_contact(self,**kw):
        print("\n\n\n\n\n\n click Create New Contact on button \n\n\n\n\n\n")
        return request.render("product_website.create_new_contact")

