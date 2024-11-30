from odoo import models, fields

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = 'Wizard to Add Attendees to a Session'

    # دالة لتحديد الجلسة الافتراضية باستخدام active_id
    def _default_session(self):
        session_id = self.env.context.get("active_id")
        return self.env['openacademy.session'].browse(session_id)

    # حقل session_id يربط الجلسة بالويدجت
    session_id = fields.Many2one("openacademy.session", string="Session", required=True, default=_default_session)

    # حقل attendee_Ids يربط المشاركين بالويدجت
    attendee_Ids = fields.Many2many("res.partner", string="Attendees")

    # دالة لإضافة المشاركين إلى الجلسة
    def add_attendees(self):
        for attendee in self.attendee_Ids:
            self.session_id.write({
                'attendee_ids': [(4, attendee.id)]  # [4, id] يعني إضافة المشاركين
            })




    def subscription(self):
        self.session_id.attendee_Ids |=self.attendee_Ids
        return {}
