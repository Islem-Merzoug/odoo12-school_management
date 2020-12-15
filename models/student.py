# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Student(models.Model):
    ''' Defining a student information '''
    _inherit = 'res.partner'
    _name="res.partner"
    _description = 'Student Information'

    gender = fields.Selection(string="Gender", selection=[('female', 'Female'), ('Male', 'male'), ], required=False, )
    nationality = fields.Char(string="Nationality", required=False, )
    course_id = fields.Many2one(comodel_name="course.course", string="Course", required=True, )
    is_student = fields.Boolean(string="is_student", default='True')