import datetime
from ast import literal_eval

from odoo import api, fields, models

# x = datetime.datetime.now()
# print(x.strftime("%m"))


class SchoolSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock = fields.Boolean("Stock")
    active = fields.Boolean(string="Active", config_parameter="school.default_active")
    partner_ids = fields.Many2many(
        "res.partner",
        "schl_partner_rel",
        "school_id",
        "partner_id",
        string="Partner Name",
    )

    @api.model
    def get_values(self):
        res = super(SchoolSettings, self).get_values()
        so = self.env["sale.order"].search([])
        print("\n\n\n\n\n\n soooo", so)

        partner_ids = (self.env["ir.config_parameter"].sudo().get_param("school.partner_ids"))
        print("\n\n\n\n======> 3 Partner Ids:: ", partner_ids)
        res.update(
            partner_ids=[(6, 0, literal_eval(partner_ids))],
        )
        return res

    def set_values(self):
        res = super(SchoolSettings, self).set_values()
        self.env["ir.config_parameter"].set_param("school.partner_ids", self.partner_ids.ids)
        return res