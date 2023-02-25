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
    note = ''

    for item in doc.items:
        items =  str(items) +"  "+str(item.description)

        if doc.items.index(item) == 0:
            note += f'{item.description} '
        else:
            note += f',{item.description}'
    doc.remarks = note

