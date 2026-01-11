from odoo import models, fields

class SpecialistJournalTemplate(models.Model):
    _name = "specialist.journal.template"
    _description = "Шаблон запису"

    name = fields.Char(string="Назва шаблону", required=True)
    content = fields.Text(string="Текст шаблону", required=True)
    active = fields.Boolean(default=True)