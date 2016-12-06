# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'aol_tender',
    'version': '0.01',
    'author': 'Simbioz',
    'category': 'other',
    'depends': ['base','crm'],
    'data': [
        'views/raw_scan.xml',
        'views/crm_lead.xml',
        'views/inherited_res_partner.xml',
        'views/inherited_res_users.xml',
        'views/menu.xml'
    ],
#    'qweb': ['static/src/xml/mail_extended.xml'],
    'installable': True,
    'auto_install': False,
}
