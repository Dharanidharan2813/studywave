frappe.ui.form.on("Lesson", {
	refresh(frm) {
		if (frappe.session.user != "Administrator") {
			let hide = frappe.user.has_role("Mentee") || false;
			frm.set_df_property("question", "hidden", hide);
		}
		frm.add_custom_button(__("Attend Q/A"), () => {
			frappe.new_doc("Quiz", {
				course: frm.doc.course_name,
				lesson: frm.doc.name,
				quiz: frm.doc.question,
			});
		});
	},
});
