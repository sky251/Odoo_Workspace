from odoo import fields, models


class SaleOrder(models.Model):
	_inherit = "school.profile"
	_description = "This is order model"

	order_name = fields.Char(string="Order name")
	order_id = fields.Char(string="Order ID")
