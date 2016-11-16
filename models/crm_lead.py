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


from openerp.osv import osv
from openerp import api, models, fields
from datetime import datetime
from openerp import tools
import logging

_mylog = logging.getLogger('YUSTAS#################################################')

'''
class note_note(models.Model):
    _inherit = 'note.note'
    
    mess_id = fields.Many2one('mail.message', string='Created from:')
    
    @api.multi
    def open_mess(self):
        if self.mess_id:
            _mylog.info("Mess id is %s" % (self.mess_id.id))
            return {
                'type': 'ir.actions.client',
                #'name': 'Inbox',
                'tag': 'mail.wall',
                'res_model': 'mail.message',
                'params': {
                    'domain':[('id','=',self.mess_id.id)],
                      'truncate_limit':10,
                      'display_intended_thread':1,
                           
                           },
               } 
    
        self.res_id = self.env['note.note'].create({'name':self.subject, 'memo':self.body, 'mess_id':self.id})
#             sent_date = self._get_date(cr, uid, rec.date, context=context)
'''