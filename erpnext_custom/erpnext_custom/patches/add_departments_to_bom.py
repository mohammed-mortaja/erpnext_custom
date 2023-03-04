import frappe


def execute():
	frappe.db.sql(""" update `tabBOM` set department = 'Accounts - ZC' where department is null """)