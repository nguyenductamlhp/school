# -*- coding: utf-8 -*-
from odoo import fields, models


class Student(models.Model):

    #_name = 'school.student' 
    _inherit = 'res.users'
    name = fields.Char('Student name',required = True)
    student_code = fields.Char('Student code',required = True)
    score = fields.Float('Student score')
    age = fields.Integer('Student age')
    is_student = fields.Boolean('Is student')
    class_id = fields.Many2one('school.class',string="Class")
    #diem -float
    #tuoi - int

