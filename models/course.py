# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.Model):
    ''' Defining a student information '''
    _inherit = 'product.template'
    _description = 'Course Information'

    is_course = fields.Boolean(string="is_course", default='True')

    # teacher_id = fields.Many2one("res.partner", string="teacher", required=False)

    def get_default_course_type(self):
        return 'is_course' in self.env.context

    is_course = fields.Boolean(default=get_default_course_type)


