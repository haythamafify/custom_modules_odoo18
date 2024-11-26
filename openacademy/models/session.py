from datetime import timedelta

from odoo import models, fields, api, exceptions
from reportlab.graphics.transform import inverse


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'openacademy.session'

    name = fields.Char(required=True)

    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digit=(6, 2), help="duration in days")
    seats = fields.Integer(string="number of seats")
    instructor_id = fields.Many2one("res.partner", string="instructor")
    course_id = fields.Many2one("openacademy.course", string="Course", required=True, ondelete="cascade")
    attendee_Ids = fields.Many2many("res.partner", string="attendee", )
    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")
    active = fields.Boolean(default=True)
    amount = fields.Float()
    unit_price = fields.Float()
    price = fields.Float()
    color = fields.Integer()
    end_date = fields.Date(string="End Date", store=True, compute="_get_end_date", inverse="_set_end_date")
    attendees_count = fields.Integer(string="Attendee Count", compute="_get_attendee_count", store=True)

    @api.depends("attendee_Ids")
    def _get_attendee_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_Ids)

    @api.depends("start_date", "end_date")
    def _get_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.end_date):
                rec.end_date = rec.start_date
                continue

            duration = timedelta(days=rec.duration, seconds=-1)
            rec.end_date = rec.start_date + duration

    def _set_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.end_date):
                continue
            rec.duration = (rec.end_date - rec.start_date).days + 1

    _sql_constraints = [
        ("name_unique", "UNIQUE('name')", "THE COURSE TITLE MUST BE UNIQUE"),
    ]

    @api.constrains("attendee_Ids", "instructor_id")
    def _check_instructor_not_in_attendee(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id in rec.attendee_Ids:
                raise exceptions.ValidationError("the session instructor can not be attendee")

    @api.onchange("seats", "attendee_Ids")
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                "warning": {
                    "title": "incorrect seats value",
                    "message": f"the number of seats may be negative : {self.seats}"
                },
            }
        # //18
        if self.seats < len(self.attendee_Ids):
            return {
                "warning": {
                    "title": " Too many attendee",
                    "message": "Increase seats or remove excess attendee"
                }
            }

    @api.onchange("amount", "unit_price")
    def _onchange_price(self):
        self.price = self.unit_price * self.amount

    @api.depends("seats", "attendee_Ids")
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_Ids) / record.seats
