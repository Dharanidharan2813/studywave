# Copyright (c) 2025, dharanidharan s and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Course(Document):
	pass


def get_courses(user=None, doctype=None):
	roles = frappe.get_roles(frappe.session.user)
	user = frappe.session.user

	if "Mentee" in roles and "System Manager" not in roles:
		escaped_user = frappe.db.escape(user)
		return f"""`tabCourse`.`name` IN (
			SELECT parent
			FROM `tabCourse User Table`
			WHERE user_name = {escaped_user}
		)"""

	if user == "Administrator":
		return
