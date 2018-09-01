from odoo import api, fields, models, _


class facultad(models.Model):
    """ facultad """

    _name = 'facultad'
    # _inherit = ''
    _description = 'facultad'

    name = fields.Char('Nombre', help=' Nombre de la facultad', required=True)

    descripcion = fields.Text('Descripcion')

    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')