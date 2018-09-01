from odoo import api, fields, models, _


class grupo(models.Model):
    """ grupo """

    _name = 'grupo'
    # _inherit = ''
    _description = 'grupo'

    numero = fields.Char('Numero', help=' Numero del grupo', required=True)

    facultad_id = fields.Many2one('facultad', 'Facultad', required=True)

    descripcion = fields.Text('Descripcion')

    @api.multi
    @api.depends('numero')
    def name_get(self):
        return map(lambda grupo: (grupo.id, grupo.numero), self)

    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')