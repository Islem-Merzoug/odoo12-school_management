# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    ''' Defining a student information '''
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string="name", required=False, )
