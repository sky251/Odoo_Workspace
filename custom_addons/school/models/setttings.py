from odoo import api, fields, models

class SchoolSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock = fields.Boolean("Stock")
    active = fields.Boolean(string="Active", config_parameter='school.default_active')


