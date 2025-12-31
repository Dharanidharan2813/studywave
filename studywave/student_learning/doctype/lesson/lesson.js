frappe.ui.form.on("Lesson", {
	refresh(frm) {
		if (frappe.session.user != "Administrator") {
			let hide = frappe.user.has_role("Mentee") || false;
			frm.set_df_property("question", "hidden", hide);
		}
		frm.add_custom_button(__("Attend Quiz"), function () {
			window.location.href = `/take-quiz?name=${frm.doc.name}`;
		});
	},
});
