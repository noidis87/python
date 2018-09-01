# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions



class listadoEstudiantes(models.TransientModel):
    _name = 'listado.estudiantes'
    _template = 'tarea_final.listado_estudiantes'
    _description = 'Listado de estudiantes'

    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha fin')
    # r_moneda = fields.Many2one(required=True)

    @api.multi
    def imprimir_reporte(self):
        result = self.env['report'].get_action(self, 'tarea_final.listado_estudiantes')
        return result