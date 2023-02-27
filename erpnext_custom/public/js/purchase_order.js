
frappe.ui.form.on("Purchase Order", {
	setup: function(frm) {

		frm.set_query("supplier2", function() {
			return{
				filters: {
					"supplier_type": ["in", ["Company"]],
				}
			}
		});
		}
		})