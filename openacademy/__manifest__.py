# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/views.xml',
        'views/partner_view.xml',
        'views/session_views.xml',
        'views/templates.xml',
        'views/session_board_views.xml',
        'wizard/wizard_view.xml',
        'reports/session_report.xml',
        # 'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
