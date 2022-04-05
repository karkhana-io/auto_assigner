import frappe

@frappe.whitelist()
def auto_assign(doc,method):
	settings = frappe.get_doc('Auto Assigner Settings')
	if not settings.enabled:
		return
	for mappings in settings.doc_mappings:
		if(mappings.doctype_1 == doc.doctype and mappings.enabled == 1):
			user_list = []
			for kv in mappings.users.split(","):
				user_list.append(kv.strip())
			
			already_assigned = frappe.db.get_list('ToDo',
					filters={
						'reference_type': doc.doctype,
						'reference_name': doc.name
					},
					fields=['owner'],
					page_length=100
				)
			
			for user in user_list:
				if not any(users.get('owner', "") == user for users in already_assigned):
					new_doc = frappe.new_doc("ToDo")
					new_doc.status = 'Open'
					new_doc.priority = 'Medium'
					new_doc.owner = user
					new_doc.description = 'Auto assigned'
					new_doc.reference_type = doc.doctype
					new_doc.reference_name = doc.name
					new_doc.insert()
			break
