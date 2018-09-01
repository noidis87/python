# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _


class profesor(models.Model):
    """ profesor """

    _name = 'profesor'
    _inherit = 'persona'

    _description = 'profesor'

    _order = 'ci'

    # name = fields.Char('Nombre', help=' Nombre de la persona', required=True)
    #
    # apellidos = fields.Char(string='Apellidos', required=True)
    #
    # edad = fields.Integer(string='Edad')
    # provincia = fields.Selection([
    #     ('pinar', 'Pinar del Rio'),
    #     ('habana', 'La Habana')], 'Provincia')
    #
    # ci = fields.Integer('Ci', size=11)
    #
    # fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    #
    # descripcion = fields.Text('Descripción')

    fecha_egreso = fields.Date(string='Fecha de graduacion')

    estudiante = fields.Many2many('estudiante', 'Estudiantes')

    dpto_id = fields.Many2one('departamento', 'Departamento', required=True)

    salario = fields.Float('Salario')
    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')
