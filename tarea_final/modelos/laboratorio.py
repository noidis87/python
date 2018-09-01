from odoo import api, fields, models, _


class laboratorio(models.Model):
    """ laboratorio """

    _name = 'laboratorio'
    # _inherit = ''
    _description = 'laboratorio'

    name = fields.Char('Numero', help=' Nombre', required=True)

    descripcion = fields.Text('Descripcion')

    tecnico_id = fields.Many2many('tecnico')
    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')