{
    'name': 'Specialist Journal',
    'version': '1.0.0',
    'category': 'Human Resources',
    'description': """
Журнал спеціаліста
Дозволяє спеціалістам вносити записи в журнал клієнта та створювати PDF-звіт з вибраними записами
Адміністратор може переглядати записи всіх спеціалістів та створювати шаблони для швидкого заповнення журналу
    """,
    'author': 'Yurii Babanskiy',
    'depends': ['base', 'contacts'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/journal_report_templates.xml',
        'views/journal_views.xml',
        'views/template_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}