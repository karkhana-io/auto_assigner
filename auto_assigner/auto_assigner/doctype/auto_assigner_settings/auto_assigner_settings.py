# Copyright (c) 2022, Karkhana.io and contributors
# For license information, please see license.txt

import json
import frappe
from frappe.model.document import Document

class AutoAssignerSettings(Document):
	def validate(self):
		check_for_duplicate_entries(self)
		
def check_for_duplicate_entries(self):
	doc_list = []
	user_list_full = []
	for entry in self.doc_mappings:
		user_list_line = []
		doc_list.append(entry.doctype_1)
		for kv in entry.users.split(","):
			user_list_line.append(kv.strip())
			user_list_full.append(kv.strip())

		if len(user_list_line) != len(set(user_list_line)):
			frappe.throw("Duplicate entries in user column")

	if len(doc_list) != len(set(doc_list)):
		frappe.throw("Duplicate entries in doctype column")
	
	check_if_user_exists(user_list_full)

def check_if_user_exists(user_list):
	user_list = set(user_list)
	users_on_system = frappe.db.get_list('User',
		filters=[
			[ 'email', 'IN', user_list]
			],
		fields=['email'],
		page_length=100
	)

	if(len(users_on_system) != len(user_list)):
		frappe.throw("Some user does not exist on system")