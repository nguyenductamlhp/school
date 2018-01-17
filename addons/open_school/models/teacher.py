# -*- coding: utf-8 -*-
from odoo import fields, models


class Teacher(models.Model):

    #_name = 'school.teacher'
    _inherit ='res.users' 
    name = fields.Char('Teacher name',required = True)
    teacher_code = fields.Char('Teacher code',required = True)
    age= fields.Integer('Teacher age')
    is_teacher = fields.Boolean('Is teacher')
    class_id = fields.Many2one('school.class',string="Class")
    

