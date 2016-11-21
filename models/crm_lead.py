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


class crm_lead(models.Model):
###Assume risk is crm_lead
#class risk_base(models.Model):
    _inherit='crm.lead'
#    _name='aol.risk.base'
    
    is_risk = fields.Boolean(string='AOL risk')
    rawscan_id = fields.Many2one(comodel_name='aol.rawscan.base', string='Origin scan')
#assum asset is res.partner
    type_id = fields.Many2one(comodel_name='aol.risk.type', string='Type of risk')
    attr_val_ids = fields.One2many(comodel_name='aol.attr.value', inverse_name='risk_id', 
                                  string='Risk attribute values')
    
   
    @api.multi  
    def create_attrs(self, **kwargs):
        attrEnv = self.env['aol.attr']
        attr_valEnv = self.env['aol.attr.value']
        for k,v in kwargs.iteritems():
            attr_rec = attrEnv.search([('name','=',unicode(k))])
            print (unicode(attr_rec))
            if not len(attr_rec):
                attr_rec = attrEnv.create({'name':unicode(k)})
            attr_valEnv.create({'value':unicode(v), 'attr_id':attr_rec.id, 'risk_id':self.id})
            
            