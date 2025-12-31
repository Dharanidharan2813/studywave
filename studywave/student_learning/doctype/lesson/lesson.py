# Copyright (c) 2025, dharanidharan s and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Lesson(Document):
	pass


@frappe.whitelist()
def check_option(ans, lesson):
	pass
	# exist = frappe.db.exists("User Log", {"student": frappe.session.user, "lesson": lesson})
	# if not exist:
	#     frappe.msgprint("Called")
	#     frappe.msgprint(ans)
	#     frappe.msgprint(lesson)

	#     ans = frappe.parse_json(ans)
	#     quizzes = frappe.get_doc('Lesson',lesson)
	#     log = frappe.new_doc('User Log')
	#     log.student = frappe.session.user
	#     log.lesson = lesson
	#     for q,answer in zip(quizzes.question, ans):
	#          new_quiz = log.append('quiz', {})
	#          new_quiz.question = q.question
	#          new_quiz.correct_answer = q.correct_answer
	#          new_quiz.answer = answer['value']
	#          new_quiz.topic = q.topic
	#          new_quiz.correct_explanation = q.correct_explanation

	#     log.insert(ignore_permissions=True)

	#     frappe.msgprint("Called")

	#     for quiz,answer in zip(quizzes.question, ans):
	#         if quiz.correct_answer == answer['value']:
	#             frappe.msgprint("Correct Answer")
	#         else:
	#             frappe.msgprint("Wrong Answer")
	# else:
	#     frappe.msgprint("You have already attempted this lesson.")
