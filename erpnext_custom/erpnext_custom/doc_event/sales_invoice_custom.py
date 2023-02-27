import frappe
from frappe.utils import time_diff_in_hours


# @frappe.whitelist()
# def validate_remarks(doc, method):
#     items = ""
#     for item in doc.get("items"):
#         items =  str(items) +"  "+str(item.item_code)
#         doc.remarks = str(items)

@frappe.whitelist()
def validate_note(doc, method):
    note = ""

    for item in doc.items:

        if doc.items.index(item) == 0:
            note += f'{item.description} '
        else:
            note += f'{item.description}'
    doc.remarks = note


@frappe.whitelist()
def validate_pos_payments(doc, method):
    total = 0
    if doc.is_pos:
        for payment in doc.payments:
            total += payment.amount 
    if total <= 0:
        frappe.throw('payment for pos invoice must be more than zero')
