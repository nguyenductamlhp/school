# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Open School',
    'version': '0.1',
    'category': 'Productivity',
    'description': """
This module update memos inside Odoo for fun
=================================================================

Use for update your text memo in real time with the following user that you invite.

""",
    'website': 'https://www.odoo.com/page/notes',
    'summary': 'Sticky memos, Collaborative',
    'depends': [
        'base',
    ],
    'data': [
        'views/student_view.xml',
        'views/class_view.xml',
        'views/teacher_view.xml',
        'views/subject_view.xml', 
        'views/session_view.xml',             
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
