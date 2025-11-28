// Copyright (c) 2025, dharanidharan s and contributors
// For license information, please see license.txt

frappe.ui.form.on("Course", {
	// refresh(frm) {

	// },
	setup: function (frm) {
		frm.set_query("enroll", function () {
			return {
				filters: { role: "Mentee" },
			};
		});
	},
});
