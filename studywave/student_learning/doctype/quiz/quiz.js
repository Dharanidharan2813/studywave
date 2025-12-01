// Copyright (c) 2025, dharanidharan s and contributors
// For license information, please see license.txt

frappe.ui.form.on("Quiz", {
	refresh(frm) {
		if (frappe.user.has_role("Mentee")) {
			let grid = frm.get_field("quiz").grid;
			grid.update_docfield_property("answer", "reqd", 1);
			grid.update_docfield_property("explanation", "reqd", 1);
			grid.update_docfield_property("correct_answer", "hidden", 1);
			grid.update_docfield_property("topic", "hidden", 1);
			grid.update_docfield_property("correct_explanation", "hidden", 1);
		}
	},
});
