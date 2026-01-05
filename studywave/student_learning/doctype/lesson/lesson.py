# Copyright (c) 2025, dharanidharan s and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Lesson(Document):
	pass


@frappe.whitelist()
def check_option(ans, lesson):
	# pass
	exist = frappe.db.exists("User Log", {"student": frappe.session.user, "lesson": lesson})
	if not exist:
		ans = frappe.parse_json(ans)
		quizzes = frappe.get_doc("Lesson", lesson)
		log = frappe.new_doc("User Log")
		log.student = frappe.session.user
		log.lesson = lesson
		log.total_marks = len(quizzes.question)
		marks = 0
		for q, answer in zip(quizzes.question, ans, strict=True):
			new_quiz = log.append("quiz", {})
			new_quiz.question = q.question
			new_quiz.correct_answer = q.correct_answer
			new_quiz.answer = answer["value"]
			new_quiz.topic = q.topic
			new_quiz.explanation = answer["explanation"]
			new_quiz.correct_explanation = q.correct_explanation
			if new_quiz.correct_answer == new_quiz.answer:
				marks += 1
		log.obtained_marks = marks
		log.insert(ignore_permissions=True)
		frappe.msgprint(_("Submitted successfully."))
	else:
		frappe.msgprint(_("You have already attempted this lesson."))
