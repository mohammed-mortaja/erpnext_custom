import frappe


@frappe.whitelist()
def create_stock_entry(doc, method):
    if doc.material_request_type == 'Material Transfer':
        new_doc = frappe.new_doc('Stock Entry')
        new_doc.stock_entry_type = 'Material Transfer'
        new_doc.from_warehouse = doc.set_from_warehouse
        new_doc.to_warehouse = doc.set_warehouse
        for item in doc.items:
            new_doc.append("items",
                           {'item_code': item.item_code, 'qty': item.qty, 's_warehouse': doc.set_from_warehouse,
                            't_warehouse': item.warehouse})

        new_doc.insert(ignore_permissions=1)
        new_doc.submit()

