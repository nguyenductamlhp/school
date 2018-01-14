# -*- coding: utf-8 -*-
from odoo import fields, models


class Student(models.Model):

    _name = 'school.student' 

    name = fields.Char('Student name',required = True)
    student_code = fields.Char('Student code',required = True)
    grade = fields.Float('Student grade')
    age = fields.Integer('Student age')
    class_id = fields.Many2one('school.class',string="Class")
    #diem -float
    #tuoi - int

