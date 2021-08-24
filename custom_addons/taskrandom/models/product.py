import random
import string
from odoo import api, fields, models
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    rndm_str = fields.Char(string=_("Random String"), compute='_compute_standard_price',
        inverse='_set_standard_price')

    @api.depends('product_variant_ids', 'product_variant_ids.rndm_str')
    def _compute_standard_price(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.rndm_str = template.product_variant_ids.rndm_str
        for template in (self - unique_variants):
            template.rndm_str = ""

    def _set_standard_price(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.rndm_str = template.rndm_str

    def random_string_generate(self):
        all_chars = list(string.ascii_letters)
        random.shuffle(all_chars)
        self.rndm_str = "".join(all_chars[:4]).upper()



class ProductProduct(models.Model):
    _inherit = "product.product"

    rndm_str = fields.Char(string=_("Random String"))

    def random_string_generate(self):
        all_chars = list(string.ascii_letters)
        random.shuffle(all_chars)
        self.rndm_str = "".join(all_chars[:4]).upper()
