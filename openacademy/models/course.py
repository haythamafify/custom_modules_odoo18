from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one("res.users", ondelete="set null", string="Responsible", index=True)

    session_ids = fields.One2many("openacademy.session", "course_id", string="Sessions")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'The Name must be Unique')
    ]
