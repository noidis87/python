from odoo import api, fields, models, _


class departamento(models.Model):
    """ departamento """

    _name = 'departamento'
    # _inherit = ''
    _description = 'departamento'

    name = fields.Char('Nombre', help=' Nombre de la persona', required=True)

    facultad_id = fields.Many2one('facultad', 'Facultad', required=True)


    descripcion = fields.Text('Descripcion')

    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')