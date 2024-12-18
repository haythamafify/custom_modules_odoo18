from datetime import date
from dateutil.relativedelta import relativedelta

# تاريخ اليوم
today = date.today()

# تاريخ الميلاد
birth_date = date(1990, 1, 8)

# حساب العمر باستخدام relativedelta
delta = relativedelta(today, birth_date)

# طباعة العمر
print(f"Age: {delta.years} years, {delta.months} months, {delta.days} days")
