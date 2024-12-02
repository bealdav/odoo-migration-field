import logging

from odoo import fields, models

from . import populate_extra_field

logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            populate_extra_field(rec)
