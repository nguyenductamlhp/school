# -*- coding: utf-8 -*-
from odoo import api,fields, models

def get_years():
        "get years for year start and end"
        year_list = []
        for i in range(1945,2100):
            year_list.append((i,str(i)))
        return year_list
class Grade(models.Model):
    _name = 'school.grade'
    _rec_name = 'grade_code'
    grade_code = fields.Char('Grade code',required = True)
    year_start = fields.Selection(get_years(),string="Start",)
    year_end = fields.Selection(get_years(),string="End",)
    class_ids = fields.One2many('school.class','grade_id',)
    _sql_constraints = [
        ('class_name_uniq', 'unique (class_ids)', "Class code already exists !"),
    ]

