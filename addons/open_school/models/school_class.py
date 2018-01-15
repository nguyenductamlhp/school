# -*- coding: utf-8 -*-
from odoo import fields, models

class School_class(models.Model):

    _name = 'school.class' 
    _rec_name = 'class_name'
    class_name = fields.Char('Class name',required = True)
    student_number = fields.Integer('Number of student',required = True)
    class_describe = fields.Text('Describe')
    student_ids = fields.One2many('school.student','class_id',)
    teacher_id = fields.Many2one('school.teacher',string="Homeroom teacher")
    _sql_constraints = [
        ('name_uniq', 'unique (class_name)', "Class name already exists !"),
    ]
