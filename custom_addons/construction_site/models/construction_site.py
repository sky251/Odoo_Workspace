from odoo import api, fields, models


class ConstructionSite(models.Model):
    _name = "construction.site"
    _description = "Construction Site"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, tracking=True)
    reference = fields.Char(string="Construction Site Code", required=True)
    display_name = fields.Char(string="Display Name", compute="_compute_display_name")
    scheduled_date = fields.Datetime(string="Material Requirement Date")

    @api.depends("name", "reference")
    def _compute_display_name(self):
        for data in self:
            data.display_name = f"[{data.reference}] {data.name}"

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("running", "Running"),
            ("stopped", "Stopped"),
            ("in_closing", "In Closing"),
            ("closed", "Closed"),
        ],
        default="draft",
        string="Status",
    )

    responsible_internal_id = fields.Many2one(
        "hr.employee", string="Internal Responsible"
    )
    responsible_on_site_id = fields.Many2one(
        "res.partner", string="On Site Responsible"
    )
    delivery_address = fields.Many2one("res.partner", string="Delivery Address")
    product_template_id = fields.Many2one("product.template", string="Product Template")
    stock_warehouse_id = fields.Many2one("stock.warehouse", string="Stock warehouse")
    project_id = fields.Many2one("project.project", string="Project")
    purchase_order_ids = fields.Many2many(
        "purchase.order",
        "purchase_construct_site",
        "purchase_id",
        "construction_id",
        string="Purchase Order",
    )
    analytical_account_id = fields.Many2one(
        "analytical.account", string="Analytical Account"
    )
    sale_order_id = fields.Many2one("sale.order", string="Sale Order")
    asset_ids = fields.Many2many(
        "account.asset",
        "asset_construct_site",
        "asset_id",
        "construction_id",
        string="Asset",
    )
    general_contractor_purchase_order_id = fields.Many2one(
        "purchase.order", string="General Contractor PO", required=True
    )

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_run(self):
        for rec in self:
            rec.state = "running"

    def action_stop(self):
        for rec in self:
            rec.state = "stopped"

    def action_in_close(self):
        for rec in self:
            rec.state = "in_closing"

    def action_close(self):
        for rec in self:
            rec.state = "closed"


    # not working
    # def open_wizard(self):
    #     print("\n\n\n\n\n\ncall wizard function 1")
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'view_id': 'construction_site_wizard_views_action',
    #         'res_model': 'construction.wizard',
    #         'target': 'new',
    #     }
