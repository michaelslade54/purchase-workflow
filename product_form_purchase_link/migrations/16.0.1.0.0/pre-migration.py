from openupgradelib import openupgrade

xml_ids = ["product_form_purchase_link.product_normal_form_view_inherit_purchase",
           "product_form_purchase_link.view_product_template_purchase_buttons_from",
           "product_form_purchase_link.purchase_order_line_search",
           "product_form_purchase_link.action_purchase_line_product_tree",
           "product_form_purchase_link.action_purchase_line_product_product_tree"]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)