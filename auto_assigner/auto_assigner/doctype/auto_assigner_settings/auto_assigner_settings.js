// Copyright (c) 2022, Karkhana.io and contributors
// For license information, please see license.txt

frappe.ui.form.on('Auto Assigner Settings', {
	onload: function(frm) {
		link_query(frm)
	}
});

function link_query(frm){
	cur_frm.fields_dict['doc_mappings'].grid.get_field("doctype_1").get_query = function(doc, cdt, cdn) {
		return {
			query: "auto_assigner.api.auto_assigner_settings.link_query_override"
		}
	}
}