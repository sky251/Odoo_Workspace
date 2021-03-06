from odoo import http
from odoo.http import request, route


class ReferalApplication(http.Controller):
    @http.route("/referral_program", type="http", website=True, auth="user")
    def referral_program(self):
        reference_id = request.env["hr.employee"].sudo().search([])
        degree_id = request.env["hr.recruitment.degree"].sudo().search([])
        department_id = request.env["hr.job"].sudo().search([])
        vals = {
            'reference_id':reference_id,
            'degree_id':degree_id,
            'department_id':department_id,

        }
        return request.render("hr_referral_application.referral_program_template",vals
        # return request.redirect('/forum/%s' % slug(forums[0]), code=302)
    
    @http.route("/submit_referral_program", type="http", website=True, auth="public")
    def submit_referral_program(self, **kw):
        if kw:
            print("kw==================",kw)
            vals = {
                'name':kw.get('name'),
                'email':kw.get('email'),
                'reference_id':kw.get('reference_id'),
                'degree_id':kw.get('degree_id'),
                'department_id':kw.get('department_id'),
                'ex_salary':kw.get('ex_salary'),
                'joining_date':kw.get('joining_date'),
                'summary':kw.get('summary'),

            }
            print("=============vals==============",vals)
            # request.env["hr.referral.application"].sudo().create(vals)

            request.env["hr.referral.application"].sudo().create(vals)
            # request.env["hr.referral.application"].sudo().create(vals)

        return request.render("hr_referral_application.thank_you_template",vals)




