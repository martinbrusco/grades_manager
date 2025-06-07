{
    'name': 'Grades Manager',
    'description': 'Sistema de gestión de notas',
    'category': 'base',
    'version': '17.0.1.0',
    'author': 'Martin Brusco',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
            'security/ir.model.access.csv',
            'views/grades_course_views.xml',
            'views/grades_res_partner_views.xml',
            'views/grades_manager_menus.xml',
            
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
