from odoo import fields, models

from . import populate_extra_field


class ResPartner(models.Model):
    _inherit = "res.partner"

    lang = fields.Selection(default="fr_FR")
    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            populate_extra_field(rec)
