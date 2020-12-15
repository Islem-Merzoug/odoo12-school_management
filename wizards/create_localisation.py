from openerp import models, fields, api

class CreateLocalisation(models.TransientModel):
        ''' Defining a wizard localisation '''
        _name = 'create.localisation'
        _description = 'create localisation Information'

        name = fields.Char(string="Name", required=True)