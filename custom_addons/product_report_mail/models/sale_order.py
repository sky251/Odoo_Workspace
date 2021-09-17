from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def mail_wizard_button(self):
        print("\n\n\n\n\n Mail Wizard Button")

    #     self.ensure_one()
    #     template_id = self._find_mail_template()
    #     lang = self.env.context.get('lang')
    #     template = self.env['mail.template'].browse(template_id)
    #     if template.lang:
    #         lang = template._render_lang(self.ids)[self.id]
    #     ctx = {
    #         'default_model': 'sale.order',
    #         'default_res_id': self.ids[0],
    #         'default_use_template': bool(template_id),
    #         'default_template_id': template_id,
    #         'default_composition_mode': 'comment',
    #         'mark_so_as_sent': True,
    #         'custom_layout': "mail.mail_notification_paynow",
    #         'proforma': self.env.context.get('proforma', False),
    #         'force_email': True,
    #         'model_description': self.with_context(lang=lang).type_name,
    #     }
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(False, 'form')],
    #         'view_id': False,
    #         'target': 'new',
    #         'context': ctx,
    #     }

    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()
        print("Productsss in order line")
        if not self.order_line:
            print("No productss")
            raise UserError(_('Pls select product'))
        return result
