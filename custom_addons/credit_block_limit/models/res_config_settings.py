import datetime
from ast import literal_eval

from odoo import api, fields, models


class ResPartnerSettings(models.TransientModel):
    _inherit = "res.config.settings"

    email = fields.Char(string="Notify Person for limit Exceed", config_parameter="credit_block_limit.email_to")

