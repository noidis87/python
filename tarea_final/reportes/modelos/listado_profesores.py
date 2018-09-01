# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions



class listadoProfesores(models.TransientModel):
    _name = 'listado.profesores'
    _template = 'tarea_final.listado_profesores '
    _description = 'Listado de profesores egresados'

    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha fin')
    # r_moneda = fields.Many2one(required=True)

    @api.multi
    def imprimir_reporte(self):
        result = self.env['report'].get_action(self, 'tarea_final.listado_profesores')
        return result