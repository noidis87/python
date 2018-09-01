# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _



class estudiantes(models.Model):
    """ estudiantes """

    _name = 'estudiante'
    _inherit = 'persona'
    _description = 'Estudiantes'

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
    # ci = fields.Float('CI', size=11, digits=(11, 0))
    #
    # fecha_nacimiento = fields.Date(string='Fecha de nacimiento')

    grupo_id = fields.Many2one('grupo', 'Grupo', required=True)

    nota = fields.Float('Nota')

    profesor = fields.Many2many('profesor','Profesores')

    fecha_ingreso = fields.Date(string='Fecha de ingreso')

    @api.multi
    def unlink(self):
        # for rec in self:
            if self.nota == 5:
                raise exceptions.ValidationError('No se puede eliminar un estudiante de 5 puntos')
            return super(estudiantes, self).unlink()


    # profesor_id = fields.Many2one('profesor', 'Profesor', domain = [('nivel','=',1)])

    # profesor_name = fields.Char(related='profesor_id.name', store=True, readonly=True)

    # profesor = fields.Many2many('profesor','Profesor')

    # estudiantes_ids = fields.One2many('profesor', 'profesor_ids')


    # @api.model
    # def create(self, vals):
    #     if vals.get('nota') <= 0.00:
    #         raise exceptions.ValidationError('Nota debe ser mayor igual que 2')
    #     return super(estudiantes, self).create(vals)


    # @api.one
    # def obtener_name(self):
    #     lista_profesor = self.env['profesor'].search([('name', '=', 'pedro')])
    #     return lista_profesor


    #
    # @api.multi
    # def lista(self):
    #     lista_profesor = self.env['profesor'].search([])
    #     return lista_profesor


    # @api.one
    # @api.constrains('fecha_ingreso', 'fecha_egerso')
    # @api.onchange()
    # def constraint_fecha(self):
    #     if self.fecha_ingreso < self.fecha_egerso:
    #         raise exceptions.ValidationError('La fecha de salida debe ser anterior a la fecha de regreso')


    # def get_balance_submayor(self, fecha_iniciosm, fecha_finsm):
    #     # sql = "SELECT l1.name,l2.name,l1.date_maturity,l1.debit,l1.credit FROM account_move_line AS l1 INNER JOIN res_partner AS l2 ON l1.partner_id = l2.id " \
    #     #       " WHERE l1.account_id = " + str(self.account_id.id) + \
    #     #       " and l1.date_maturity >= '" + fecha_iniciosm + "' and l1.date_maturity <= '" + fecha_finsm + "'"
    #     # # "' and l1.currency_id = '" + self.moneda.id +
    #     # self.env.cr.execute(sql)
    #     # lista_account_move_line = [t for t in self.env.cr.fetchall()]
    #     lista_account_move_line = self.env['account.move.line'].search(
    #         [('account_id', '=', self.account_id.id), ('date_maturity', '>', self.fecha_iniciosm),
    #          ('date_maturity', '<', self.fecha_finsm), ('currency_id', '=', self.moneda.id)])
    #     list_vacia = []
    #     if len(lista_account_move_line)==0:
    #         list_vacia.insert(0,0)
    #         list_vacia.insert(1,0)
    #         list_vacia.insert(2,0)
    #         list_vacia.insert(3,0)
    #         return list_vacia
    #     aux = 0.00
    #     lista_objetos = []
    #     lista_aux = []
    #     for move_line in lista_account_move_line:
    #         debit = move_line[3] + move_line[4]
    #         credit = move_line[3] + move_line[4]
    #         total = debit - credit
    #         cuentas_total = {
    #             'name': move_line[0],
    #             'partner': move_line[1],
    #             'date_maturity': move_line[2],
    #             'debit': move_line[3],
    #             'credit': move_line[4],
    #             'total': aux + (move_line[3] - move_line[4])}
    #         lista_objetos.append(cuentas_total)
    #         aux = aux + (move_line[3] - move_line[4])
    #         lista_aux.insert(0, lista_objetos)
    #         lista_aux.insert(1, debit)
    #         lista_aux.insert(2, credit)
    #         lista_aux.insert(3, total)
    #     return lista_aux

