from odoo import models, fields, api

class SpecialistJournal(models.Model):
    _name = "specialist.journal"
    _description = "Journal Entry"
    _order = "date desc"

    date = fields.Datetime(string="Дата", default=fields.Datetime.now, required=True)
    user_id = fields.Many2one("res.users", string="Спеціаліст", default=lambda self: self.env.user, required=True)
    partner_id = fields.Many2one("res.partner", string="Клієнт", required=True, ondelete="cascade")
    note = fields.Text(string="Запис")
    template_ids = fields.Many2many("specialist.journal.template", string="Шаблони")

    @api.onchange('template_ids')
    def _onchange_template_ids(self):
        if self.template_ids:
            new_text = self.template_ids[-1].content
            if new_text:
                self.note = f"{self.note or ''}\n\n{new_text}".strip()
            self.template_ids = [(5, 0, 0)]