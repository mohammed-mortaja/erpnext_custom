import frappe

# def validate_reason_for_leaving(doc , method):
#    if doc.status == 'Left' :
#       if not doc.reason_for_leaving:
#          frappe.throw("must be enter reason_for_leaving")


def validate_create_task(doc , method):
    if doc.status == 'Left':
        task_doc = frappe.new_doc("Task")
        task_doc.subject="end of serv " + str(doc.employee_name)
        task_doc.employee_responsible = doc.employee_responsible
        task_doc.insert()