from odoo import models, fields, api
import logging


class Course(models.Model):
    ''' Defining a classe information '''
    _name = 'classe.classe'
    _description = 'classe Information'

    name = fields.Char(string="Name", required=True)
    fromm = fields.Datetime(string="From", required=True)
    too = fields.Datetime(string="To", required=True)
    service_id = fields.Many2one("product.template", string="Service", required=True)

    teacher_id = fields.Many2one("res.users", string="Teacher", required=False)
    localisation = fields.Selection(string="Localisation",
                                    selection=[('salle1', 'Salle1'), ('salle2', 'Salle2'), ('salle3', 'Salle3'), ],
                                    required=False)
    localisation_id = fields.Many2one("classe.localisation", string="Localisation", required=False)
    availisable_space = fields.Integer(string="", required=False)
    students_ids = fields.Many2many("student.student", string="Student", required=False)

    # it_repeats_weekly = fields.Boolean("it repeats weekly")
    it_repeats_weekly = fields.Char(string="repeats weekly", required=False, )

    Saturday = fields.Boolean(string="Saturday")
    Sunday = fields.Boolean(string="Sunday")
    Monday = fields.Boolean(string="Monday")
    tuesday = fields.Boolean(string="tuesday")
    wednesday = fields.Boolean(string="wednesday")
    thursday = fields.Boolean(string="thursday")
    friday = fields.Boolean(string="friday")

    # it_repeats_monthly = fields.Boolean("it repeats monthly")
    it_repeats_monthly = fields.Char(string="repeats monthly", required=False, )
    it_repeats_daily = fields.Char(string="repeats daily", required=False, )

    monthly_dates = fields.Date(string="Monthly Dates", required=False, )

    repeats = fields.Selection(string="Repeats",
                               selection=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ],
                               required=False)
    @api.one
    @api.onchange('repeats')
    def onchange_repeats_weekly(self):
        if self.repeats == 'monthly':
            self.it_repeats_monthly = 'monthly'
            self.it_repeats_weekly = ''
            self.it_repeats_daily = ''
            _logger.debug(it_repeats_monthly)

        if self.repeats == 'weekly':
            self.it_repeats_monthly = ''
            self.it_repeats_weekly = 'weekly'
            self.it_repeats_daily = ''

        if self.repeats == 'daily':
            self.it_repeats_monthly = ''
            self.it_repeats_weekly = ''
            self.it_repeats_daily = 'daily'
        #
        # if self.repeats == 'weekly':
        #     self.it_repeats_weekly = False



            # self.it_repeats_monthly = 'monthly'
            # self.it_repeats_weekly = 'weekly'
            # self.it_repeats_daily = 'daily'

        # if self.repeats == 'daily':
        #     self.it_repeats_weekly = 'False'

class Localisation(models.Model):
    ''' Defining a classe localisation '''
    _name = 'classe.localisation'
    _description = 'classe localisation Information'

    name = fields.Char(string="Name", required=True)
