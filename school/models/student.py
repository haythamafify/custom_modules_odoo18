from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError  # استيراد ValidationError


class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Student Name", )
    amount = fields.Float(string="Fees", )
    department_id = fields.Many2one("student.departments", string="Department Name", )
    subject_ids = fields.Many2many("student.subjects", "subject_student_rel", string="Subjects")
    result_student_ids = fields.One2many("student.result", "student_id", string="Results")
    age = fields.Integer(string="Age", compute="get_age", store=True)
    date_of_birth = fields.Date(string="Date of Birth", )
    is_student = fields.Boolean(string="Is Student", default=True)

    @api.depends("date_of_birth")
    def get_age(self):
        """
        Computes the age of the student based on their date of birth.
        The age is computed as the difference between the current date and
        the student's date of birth.
        """
        for student in self:
            if student.date_of_birth:
                today = date.today()
                birth_date = fields.Date.from_string(student.date_of_birth)
                delta = relativedelta(today, birth_date)
                student.age = delta.years
            else:
                student.age = 0  # If no birth date is provided, age is set to 0


class Departments(models.Model):
    _name = "student.departments"
    _description = "Department"

    name = fields.Char(string="Department Name", )
    address = fields.Char(string="Address")


class Subjects(models.Model):
    _name = "student.subjects"
    _description = "Subject"

    name = fields.Char(string="Subject Name", )


class Result(models.Model):
    _name = "student.result"
    _description = "Student Result"

    student_id = fields.Many2one("student.student", string="Student", )
    result = fields.Float(string="Result", )
    subject_id = fields.Many2one("student.subjects", string="Subject", )

    @api.constrains('result')
    def check_result_range(self):
        """
        Ensures that the result is between 0 and 100.
        """
        for record in self:
            if not (0 <= record.result <= 100):
                raise ValidationError("Result must be between 0 and 100.")