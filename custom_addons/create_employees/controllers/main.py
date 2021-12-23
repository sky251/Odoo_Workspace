from odoo import http
from odoo.http import request, route
import base64

class CreateEmployees(http.Controller):
    @http.route("/create_employees", type="http", website=True, auth="user", csrf=False)
    def create_emp(self, **kw):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        job_position = request.env["hr.job"].sudo().search([])
        return request.render("create_employees.craete_employees_template",
                              {"countries": countries, "states": states, "job_position": job_position})

    @http.route("/create_emp", type="http", website=True, auth="user", csrf=False)
    def new_employee_create(self, **kw):

        # doc = kw.get("documents")
        # print("\n\n\n\n\n doc ", doc)
        # data_bytes = doc.encode("utf-8")
        # documents = base64.b64encode(data_bytes)
        # print("\n\n\n\n\n doc ", type(documents))
        # print("\n\n\n\n\n kw",kw)
        # kw.update(
        #     {
        #         "documents": documents,
        #     }
        # )
        print("\n\n\n\n\n kw", kw)
        Attachments = request.env['ir.attachment']
        # name = kw.get('documents')

        file = kw.get('documents')

        attachment = file.read()
        attachment_id = Attachments.sudo().create({
            'name': file,
            'datas_fname': name,
            'res_name': name,
            'type': 'binary',
            'res_model': 'create.employees',
            'datas': attachment.encode('base64'),
        })
        kw.update(
            {
                "documents": attachment_id,
            }
        )


        # d_o_b = kw.get("d_o_b")
        # street = kw.get("street")
        # state = kw.get("state_id")
        # country = kw.get("country_id")
        # city = kw.get("city")
        # email = kw.get("email")
        # phone = kw.get("phone")
        # gender = kw.get("gender")
        # # phone = kw.get("phone")
        # exp_info = kw.get("experience_info")
        # exp_sal = kw.get("expected_salary")
        # jp = kw.get("job_position_id")


        # print(
        #     f"\n\n\n\n name:{name}\n,dob:{d_o_b}\n,street:{street}\n,sate:{state}\n,country: {country}\n,city :{city}\n,email: {email}\n,Phone :{phone}\n,gender: {gender}\n,exp_info : {exp_info}\n,exp_sal :{exp_sal}\n,jp:{jp}")
        if kw:
            print(kw)
            employee = request.env["create.employees"].sudo().create(kw)
        # return request.redirect("/create_employees")

    @http.route("/employee_details", type="http", website=True, auth="user", csrf=False)
    def employee_details(self, **kw):
        job_position = request.env["hr.job"].sudo().search([])
        values = {"job_position": job_position, 'submit': False}
        if kw:
            jp, filtered_employee = False, False
            if kw.get('job_position'):
                jp = int(kw.get('job_position'))
                filtered_employee = request.env["create.employees"].sudo().search([('job_position', '=', jp)])
            values.update({'submit': True, 'filtered_employee': filtered_employee, 'jp': jp})
        return request.render("create_employees.employee_details_template", values)

    @http.route(["/my/check_existing_order", "//my/check_existing_order/<int:page>"], type='http', auth="user",
                website=True)
    def portal_menu(self):
        pass
