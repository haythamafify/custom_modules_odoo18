from odoo import models, fields, api


class Student(models.Model):
    _name = "student.student"
    name = fields.Char(string="Student Name")
    amount = fields.Float(string="Fees")
    # many student one department
    department_id = fields.Many2one("student.departments", string="Department Name")
    subject_ids = fields.Many2many("student.subjects", "subject_student_rel", string="subject Name")
    result_student_ids = fields.One2many("student.result", "student_id", string="Results")
    age = fields.Integer(string="Age", compute="get_age", store=True)
    date_of_birth = fields.Date(string="Date Of Birth")

    @api.depends("date_of_birth")
    def get_age(self):
        for student in self:
            if student.date_of_birth:
                today = date.today()
                birth_date = fields.Date.from_string(student.date_of_birth)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                student.age = age
            else:
                student.age = 0


class Departments(models.Model):
    _name = "student.departments"
    name = fields.Char(string="Department Name")
    address = fields.Char(string="Address")


class Subjects(models.Model):
    _name = "student.subjects"
    name = fields.Char(string="subject Name")


class Result(models.Model):
    _name = "student.result"

    student_id = fields.Many2one("student.student")

    result = fields.Float(string="Result")
    subject_id = fields.Many2one("student.subjects")
