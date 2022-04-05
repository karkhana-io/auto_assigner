import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def link_query_override(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
	return frappe.db.sql("""
			SELECT
				`tabDocType`.name
			FROM
				`tabDocType`
			WHERE 
				( `tabDocType`.`name` LIKE %(txt)s AND 
                    `tabDocType`.`is_submittable` = 1 )
			ORDER BY
				`tabDocType`.`%(key)s`
			""" % {
				"key": searchfield,
				"start": start,
				"page_len": page_len,
			"txt": "%(txt)s"
		}, {"txt": ("%%%s%%" % txt)}, as_dict=as_dict)