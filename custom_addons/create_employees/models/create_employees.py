from datetime import datetime
from dateutil import relativedelta
from odoo import api, fields, models


class CreateEmployees(models.Model):
    _name = 'create.employees'
    _description = 'CreateEmployees'

    name = fields.Char(string="Name", required=True)
    d_o_b = fields.Date(string="Birth Date")
    age = fields.Char(string="Age")
    street = fields.Char(string="Street")
    state = fields.Many2one("res.country.state", string="State")
    country = fields.Many2one("res.country", string="Country")
    city = fields.Char(string="City")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )

    experience_info = fields.Text(string="Experience Info")
    expected_salary = fields.Integer(string="Expected Salary")
    job_position = fields.Many2one("hr.job", string="Job Position")
    affordable_salary = fields.Integer(related="job_position.affordable_salary", string="Affordable Salary")
    extra_amount = fields.Float(string="Extra Amount")
    # yearly_amount = fields.Float(compute='_compute_calculate_month', string="Yearly Amount", readonly=True)
    yearly_amount = fields.Float(string="Yearly Amount", readonly=True)
    monthly_amount = fields.Float(string="Monthly Amount", readonly=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    documents = fields.Binary(string="Documents")



    def calculate_amount(self):
        print("\n\n\n\n\nON Change Calling")
        r = relativedelta.relativedelta(self.end_date, self.start_date)
        month = r.months
        year = r.years

        if year == 0 and month >= 1:  # Monthly Calculation : Expected salary + Extra Amount + Affordable Salary = Monthly Amount
            self.monthly_amount = self.expected_salary + self.extra_amount + self.affordable_salary

        elif year >= 1:  # Yearly Calculation Yearly Amount = Expected salary + Extra Amount
            self.yearly_amount = self.extra_amount + self.expected_salary
