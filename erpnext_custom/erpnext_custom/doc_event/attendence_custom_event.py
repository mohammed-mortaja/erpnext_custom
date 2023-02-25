import frappe
from frappe.utils import time_diff_in_hours


@frappe.whitelist()
def validate_attendance_hours(doc, method):
    doc.hours = float(time_diff_in_hours(doc.check_out, doc.check_in))
    if not doc.check_out or not doc.check_in:
        doc.hours = 0
        doc.status = "Absent"