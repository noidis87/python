# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tarea final',
    'version': '1.0',
    'summary': 'Tarea final',
    'description': """Tarea final""",
    'category': 'Tarea final',
    'website': 'fenixerp@uci.cu',
    'images': [],
    'depends': [       
    ],
    'data': [ 'vistas/menu.xml',
              'vistas/persona.xml',
              'vistas/profesor.xml',
              'vistas/estudiantes.xml',
              'vistas/departamento.xml',
              'vistas/facultad.xml',
              'vistas/grupo.xml',
              'vistas/tecnico.xml',
              'vistas/laboratorio.xml',
              'reportes/data/reportes_data.xml',
              'reportes/wizard/listado_estudiantes_wizard.xml',
              'reportes/wizard/listado_profesores_w.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True
}

