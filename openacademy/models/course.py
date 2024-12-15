from email.policy import default

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one("res.users", ondelete="set null", string="Responsible", index=True)

    session_ids = fields.One2many("openacademy.session", "course_id", string="Sessions")
    state = fields.Selection([
        ("draft","Draft"),
        ("submitted","Submitted"),
        ("department_manger_approve","Department Manger Approve"),
        ("dean_of_the_college_approve","Dean of the college Approve"),
        ("disapprove","Disapproved"),
    ],string="Course Status",readonly=True,copy=False,default="draft")
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'The Name must be Unique')
    ]

    def action_submit(self):
        print("action_submit")
