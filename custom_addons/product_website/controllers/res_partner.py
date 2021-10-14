import json

from odoo import http
from odoo.http import request, route


class ContactController(http.Controller):
    @http.route("/contact/", type="http", website=True, auth="public")
    def contact_details(self, **kw):
        contacts = request.env["res.partner"].sudo().search([])
        return request.render("product_website.contacts_list", {"contacts": contacts})

    @http.route(
        "/contact/<model('res.partner'):partner>/",
        type="http",
        website=True,
        auth="public",
    )
    def button_click(self, partner):
        print("\n\n\n\n\n\n click Res Contact on button \n\n\n\n\n\n")
        return request.render(
            "product_website.contacts_form_views", {"partner": partner}
        )

    @http.route(
        "/contact/create_new_contact/", type="http", website=True, auth="public"
    )
    def create_new_contact(self, **kw):
        print("\n\n\n\n\n\n click Create New Contact on button \n\n\n\n\n\n")
        return request.render("product_website.create_new_contact")

    @http.route("/partner_update", type="http", website=True, auth="public", csrf=False)
    def partner_update(self, **kw):
        print("\n\n\n\n\n\n click Create New Contact on button \n\n\n\n\n\n")
        partner = request.env["res.partner"].sudo().browse(int(kw.get("id")))
        partner.write(
            {
                "name": kw.get("name"),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }
        )
        print("\n\n\n\n\n\n click Create New Contact on button \n\n\n\n\n\n", partner)
        return request.redirect("/contact/%s" % partner.id)

    @http.route("/create_new_cont", type="http", website=True, auth="public")
    def crt_new_cont(self, **kw):
        # contacts = request.env["res.partner"].sudo().search().read(["email"])
        em = request.env["res.partner"].search([]).read(["email"])
        email_list = []
        for e in em:
            email_list.append(e["email"])
        email = kw.get("email")
        if email in email_list:
            print("\n\n\n\n\n\n Email already used \n\n\n\n\n\n")
            return request.render("product_website.create_new_contact")
        else:
            print("\n\n\n\n Else part \n\n\n")
            vals = {
                "name": kw.get("name"),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }

            print("=============vals==============", vals)
            request.env["res.partner"].sudo().create(vals)
            return request.redirect("/contact/")

        return request.render("product_website.create_new_contact")
