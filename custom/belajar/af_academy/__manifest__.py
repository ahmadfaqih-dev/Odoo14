# -*- coding: utf-8 -*-
{
    'name': "Belajar Odoo",

    'summary': """
        Belajar Odoo Dasar custom module tentang academy""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ahmad Faqih",
    'website': "https://ahmadfaqih-dev.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_menu.xml',
        'views/course_views.xml',
        'views/course_categ_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
