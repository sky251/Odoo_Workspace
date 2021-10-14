from openerp.exceptions import ValidationError

from odoo import api, fields, models


class SchoolProfile(models.Model):
    _name = "school.profile"
    _description = "School Information"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # _rec_name = "name"

    @api.depends("courses")
    def _compute_course_wise_salary(self):
        for cor in self:
            if cor.courses == "computer":
                cor.salary = 28000
            elif cor.courses == "electrical":
                cor.salary = 30000
            elif cor.courses == "automobile":
                cor.salary = 32000
            elif cor.courses == "civil":
                cor.salary = 27000
            else:
                cor.salary = 10000

    name = fields.Char(
        string="School name",
        help="Write a school name",
        index=True,
    )
    type = fields.Selection(
        [("public", "Public"), ("private", "Private")], string="Type"
    )
    email = fields.Char(string="Email", default="xyz@gmail.com")
    phone = fields.Char(string="Phone")
    parking = fields.Boolean(string="Parking")
    result = fields.Float(string="Result")
    fees = fields.Integer(string="Fees")
    salary = fields.Integer(
        compute="_compute_course_wise_salary",
        string="Salary",
        readonly=True,
        store=True,
    )
    school_address = fields.Text(string="School address")
    establish_date = fields.Date(string="Establish date")
    open_date = fields.Datetime(string="open date")
    courses = fields.Selection(
        [
            ("computer", "Computer"),
            ("automobile", "Auto Mobile"),
            ("civil", "Civil"),
            ("mechanical", "Mechanical"),
            ("electrical", "Electrical"),
        ],
        string="Course selection",
    )
    documents = fields.Binary(string="Documents")
    docu_name = fields.Char(string="Documents name")
    image = fields.Binary(attachment=True, store=True)
    image_name = fields.Char(string="Image Name", invisible="1")
    school_desc = fields.Html(string="School description")
    student_data_ids = fields.One2many(
        "student.profile", "school_select_id", string="Student data"
    )
    # student_data_id = fields.Many2one('student.profile', string='Studeadfasdnt data')
    delivery_count = fields.Integer(
        string="Delivery Orders", compute="_compute_picking_ids"
    )
    total_student_count = fields.Integer(
        string="Total Student", compute="_compute_count_total_student"
    )
    seq = fields.Integer(default=1)

    _sql_constraints = [
        (
            "name_unique",
            "unique(name)",
            "please enter unique school name, Given school name already exists.",
        ),
        (
            "notnull_order_line",
            "CHECK((email IS NOT NULL AND phone IS NOT NULL) OR (email IS NULL))",
            "The Project Sale Order Items.",
        ),
    ]

    # ('email_unique',
    #  'unique(email)',
    #  "please enter unique email id, Given email id already exist."),
    #
    # ('phone_unique',
    #  'unique(phone)',
    #  "please enter another phone number, Given phone number already exist.")

    # @api.constrains('result')
    # def _check_something(self):
    #     for record in self:
    #         if record.result < 33.0:
    #             raise ValidationError("YOU ARE FAIL!!!!")

    def button_on_click(self):
        print("smart button click")

    @api.depends("delivery_count")
    def _compute_picking_ids(self):
        for stud in self:
            stud.delivery_count = self.env["student.profile"].search_count(
                [("school_select_id.id", "=", self.id)]
            )

    def button_click(self):
        print("smart button click")
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "student",
            "view_mode": "tree",
            "res_model": "student.profile",
            "domain": [("school_select_id.id", "=", self.id)],
        }

    @api.model
    def name_create(self, name):
        print("name_create calling...", name)
        rtn = super(StudentProfile, self).name_create(name)
        return rtn
