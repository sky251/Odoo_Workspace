from odoo import fields, models
from odoo.tools.translate import _

class SaleOrder(models.Model):
	_inherit = "sale.order"

	total_capacity = fields.Float(string=_("Total Capacity"))

class SaleOrderLine(models.Model):
	_inherit = "sale.order.line"

	max_qty_allowed = fields.Float(string=_("Max Qty Allowed"), readonly=True)
