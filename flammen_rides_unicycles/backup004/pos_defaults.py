"""Default values and validation options for point-of-sale checkout."""

import re

BASE_PRICE = 450.00

US_STATE_CODES = frozenset("""
    AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN
    MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA
    WA WV WI WY DC
    """.split())
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
ZIP_CODE_PATTERN = re.compile(r"\d{5}(?:-\d{4})?")

SHIPPING_METHODS = {
    "1": {"name": "Standard Ground", "cost": 25.00, "days": "3-5 business days"},
    "2": {"name": "Express 2-Day", "cost": 55.00, "days": "2 business days"},
    "3": {"name": "Overnight Freight", "cost": 95.00, "days": "1 business day"},
}
