from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    journal_ids = fields.One2many("specialist.journal", "partner_id", string="Записи в журналі")