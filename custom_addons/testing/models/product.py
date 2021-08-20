from odoo import api, models, fields
from odoo.tools.translate import _


class ProductProduct(models.Model):
	_inherit = "product.product"

	qty_on_order = fields.Float(string=_("Qty On Order"), default=1.0)
