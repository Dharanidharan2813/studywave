# Copyright (c) 2025, dharanidharan s and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Quiz(Document):
	pass


def has_permission(user=None):
	if not user:
		user = frappe.session.user

	if "Mentor" in frappe.get_roles(user):
		return ""

	else:
		return f"tabQuiz.user = '{user}'"


def has_permission_record(doc, user):
	if not user:
		user = frappe.session.user

	if "Mentee" in frappe.get_roles(user):
		return doc.user == user
