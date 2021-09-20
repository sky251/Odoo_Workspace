from odoo import api, fields, models

class SchoolSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock = fields.Boolean("Stock")
    active = fields.Boolean(string="Active", config_parameter='school.default_active')
    partner_ids = fields.Many2many("res.partner","schl_partner_rel","school_id","partner_id",string="Partner Name")


