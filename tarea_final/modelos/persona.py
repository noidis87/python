from odoo import api, fields, models, _


class persona(models.Model):
    """ persona """

    _name = 'persona'
    # _inherit = ''
    _description = 'persona'

    name = fields.Char('Nombre', help=' Nombre', required=True)

    image = fields.Binary('Foto')

    apellidos = fields.Char(string='Apellidos', required=True)

    edad = fields.Integer(string='Edad')

    provincia = fields.Selection([
        ('pinar', 'Pinar del Rio'),
        ('habana', 'La Habana'),
        ('stgo', 'Santiago de Cuba'),
        ('gtmo', 'Guantanamo'),
        ('tunas', 'Las Tunas'),
        ('hol', 'Holguin'),
        ('gran', 'Granma')], 'Provincia')

    ci = fields.Float('CI', size=11, digits=(11, 0))

    facultad_id = fields.Many2one('facultad', 'Facultad', required=True)

    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')




    # , compute = "calcular_salario"
    # profesor_ids = fields.Many2one('estudiantes')