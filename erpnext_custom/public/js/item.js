
frappe.ui.form.on('Item',{
    refresh: function(frm) {

        if (frm.doc.is_stock_item) {

        frm.add_custom_button(__('Work Order'), function() {
            frappe.route_options = {
                "production_item": frm.doc.name
            }
            frappe.set_route("List", "Work Order");
        });

    }

    },


})