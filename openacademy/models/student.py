from odoo import models, fields


class Student(models.Model):
    _name = "student"
    name = fields.Char(string="Student Name")
    amount = fields.Float(string="Fees")
    department_id = fields.Many2one("department", string="Department Name")
    subject_ids = fields.Many2many("subject", "subject_rel", string="subject Name")


class Department(models.Model):
    _name = "department"
    name = fields.Char(string="Department Name")


class Subject(models.Model):
    _name = "subject"
    name = fields.Char(string="subject Name")
# t 41.
