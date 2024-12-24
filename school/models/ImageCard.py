from odoo import models, fields, api
from PIL import Image
from io import BytesIO


class ImageCard(models.Model):
    _name = 'image.card'
    _description = 'Image Card'
    name = fields.Char(string="الاسم", required=True)
    phone = fields.Char(string="رقم الهاتف", required=True)
    card_id = fields.Char(string="رقم البطاقة", required=True, size=10)
    image = fields.Binary(string="الصورة الشخصية")
    receipt_image = fields.Binary(string="صورة الإيصال")
    text = fields.Text(string="ملاحظات")
