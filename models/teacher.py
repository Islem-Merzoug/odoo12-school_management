# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Teacher(models.Model):
    ''' Defining a student information '''
    _inherit = 'res.partner'
    _description = 'Student Information'


