from odoo import api, fields, models


class SchoolData(models.AbstractModel):
    _name = 'report.school.report_school_data_detail'
    _description = 'School Record'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n===> _get_report_callingggg", self)
        print("\n\n\n===> docids_callingggg", docids)

        docs = self.env['school.profile'].browse(docids)
        students = self.env['student.profile'].search([('school_select_id.id', '=', docids[0])])
        students_list = []
        for stu in students:
            st_name = stu.name
            students_list.append(st_name)
        print("student id", students)
        print("student list", students_list)
        return {
            'doc_model': 'school.profile',
            'data': data,
            'docs': docs,
            'students_list': students_list,
        }
