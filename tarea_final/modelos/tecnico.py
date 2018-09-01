from odoo import api, fields, models, _


class tecnico(models.Model):
    """ tecnico """

    _name = 'tecnico'
    _inherit = 'persona'
    _description = 'tecnico'

    # name = fields.Char('Nombre', help=' Nombre del tecnico', required=True)

    laboratorio_id = fields.Many2many('laboratorio')

    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')