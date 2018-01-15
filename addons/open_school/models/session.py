# -*- coding: utf-8 -*-
from odoo import api,fields, models
from odoo.exceptions import	ValidationError


class Session(models.Model):

    _name = 'school.session' 
    session_code = fields.Char('Session code')
    date_start = fields.Date('Start')
    date_end = fields.Date('End')
    teacher_id = fields.Many2one('school.teacher',string="Teacher")
    subject_id = fields.Many2one('school.subject',string="Subject")
    class_id = fields.Many2one('school.class',string="Class")
    _sql_constraints = [
        ('name_uniq', 'unique (session_code)', "Session code already exists !"),
    ]
    @api.constrains('date_end')
    def _checkdate(self):
        for school in self:
            if(school.date_end <= school.date_start):
                raise ValidationError("End-date must be greater than Start-date!")