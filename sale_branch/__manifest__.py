# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Sales Branches",

    'summary': "Adding branch field to sale order, prioritze order by branch sequence",

    'description': """
        Custom feature: adding branch field to sales and accounting/invoice application
    """,

    'category': 'Hidden',
    'version': '0.1',

    'depends': ['sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/sale_order_branch_views.xml',
        'views/sale_order_branch_menus.xml',
    ],
    'auto_install': False,
    'license': 'OEEL-1',
}
