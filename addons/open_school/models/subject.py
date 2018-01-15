# -*- coding: utf-8 -*-
from odoo import fields, models


class Subject(models.Model):

    _name = 'school.subject' 
    _rec_name = 'subject_name'
    subject_name = fields.Char('Subject name',required = True)
    subject_code = fields.Char('Subject code',required = True)
    subject_duration = fields.Integer('Subject duration')
    subject_describe = fields.Text('Subject describe')
    _sql_constraints = [
        ('name_uniq', 'unique (subject_name)', "Session code already exists !"),
        ('name_uniq', 'unique (subject_code)', "Session code already exists !"),
    ]
