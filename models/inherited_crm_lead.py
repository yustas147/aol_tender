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

    @api.multi
    def _get_vuln_id(self):
        #res = self.vuln_ids[0].mapped('id')
       # _mylog.info('res _get_vuln_id: %s' % (unicode(res)))
        if len(self.vuln_ids):
            self.vuln_id = self.vuln_ids[0]
        #return res
        
    @api.multi
    def _get_phish_id(self):
        if len(self.phish_ids):
            self.phish_id = self.phish_ids[0]
        #return res

    
    is_risk = fields.Boolean(string='AOL risk')
    rawscan_id = fields.Many2one(comodel_name='aol.rawscan.base', string='Origin scan')
#assum asset is res.partner
    type_id = fields.Many2one(comodel_name='aol.risk.type', string='Type of risk')
    attr_val_ids = fields.One2many(comodel_name='aol.attr.value', inverse_name='risk_id', 
                                  string='Risk custom attribute values')
    date_f = fields.Datetime(string="Date of finding")
    
    vuln_ids = fields.One2many(comodel_name='aol.risk.vuln', inverse_name='crm_lead_id', 
                              string='Detailed risk record')
    phish_ids = fields.One2many(comodel_name='aol.risk.phishing', inverse_name='crm_lead_id', 
                              string='Detailed risk record')
    vuln_id = fields.Many2one(comodel_name='aol.risk.vuln', compute=_get_vuln_id)
    phish_id = fields.Many2one(comodel_name='aol.risk.phishing', compute=_get_phish_id)
#    vuln_id = fields.Many2one(comodel_name='aol.risk.vuln', compute=_get_vuln_id)
    a_user_id = fields.Many2one(comodel_name='res.users', string="Assoc. User")
    
    
   
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
            
    @api.multi
    @api.onchange('type_id')
    def _onchange_risk_type(self):
        attr_val_env = self.env['aol.attr.value']
        o2m_vals=[]
        for attrib in self.type_id.risk_attr_ids:
            #print unicode(attrib)
   #         _mylog.info(unicode(attrib))
            if attrib not in [attr_val.attr_id for attr_val in self.attr_val_ids]:
                _mylog.info(unicode(attrib))
                #attr_val_env.create({'value':False, 'risk_id':self.id, 'attr_id':attrib.id})
                o2m_vals.append((0,0,{'value':False, 'risk_id':self.id, 'attr_id': attrib.id}))
        self.update({'attr_val_ids':o2m_vals})
                
class risk_phishing(models.Model):
    _name="aol.risk.phishing"    
    _inherits={'crm.lead':'crm_lead_id'}    
    
    clicks_num = fields.Integer(string="Clicks number")
    multi_email_open = fields.Boolean(string="Multi Email Opened")
    multi_click_event = fields.Boolean(string="Multi Click Event")
    
class risk_vulnerability(models.Model):
    _name="aol.risk.vuln"    
    _inherits={'crm.lead':'crm_lead_id'}    
    
    service_port = fields.Char(string="Asset port")
    asset_ip = fields.Char(string="Asset IP")
    asset_os = fields.Char(string="OS")
    asset_os_ver = fields.Char(string="Os Ver")
#    vuln_sev_lev = fields.Char(_compute='_get_sev_rating', string='Severty Rating')
    vuln_sev_lev = fields.Selection(compute='_get_sev_rating', string='Severty Rating', selection=[('none','None'),('low','Low'),('critical','Critical'),('high','High'),('medium','Medium')])
#    sev_lev = fields.Selection(_compute='_get_sev_rating', string='Severty Rating', selection=[('none','None'),('low','Low'),('critical','Critical'),('high','High'),('medium','Medium')])
    service_name = fields.Char(string="Service name")
    plugin_name = fields.Char(string="Plugin name")
    plugin_id = fields.Char(string="Plugin id")
    vuln_risk_score = fields.Float(string="CVSS")

    @api.depends('vuln_risk_score')    
    def _get_sev_rating(self):
        _mylog.info('#################### _get_sev_lev fired!')
        for rec in self:
            if float(rec.vuln_risk_score) <= 0.01:
                rec.vuln_sev_lev = 'none'
            elif float(rec.vuln_risk_score) <= 2:
                rec.vuln_sev_lev = 'low'
            elif float(rec.vuln_risk_score) <= 4:
                rec.vuln_sev_lev = 'medium'
            elif float(rec.vuln_risk_score) <= 6:
                rec.vuln_sev_lev = 'high'
            else:
                rec.vuln_sev_lev = 'critical'
        return True
            
        
    
    @api.multi  
    def create_attrs(self, **kwargs):
        attrEnv = self.env['aol.attr']
        attr_valEnv = self.env['aol.attr.value']
        for k,v in kwargs.iteritems():
            attr_rec = attrEnv.search([('name','=',unicode(k))])
            print (unicode(attr_rec))
            if not len(attr_rec):
                attr_rec = attrEnv.create({'name':unicode(k)})
            attr_valEnv.create({'value':unicode(v), 'attr_id':attr_rec.id, 'risk_id':self.crm_lead_id.id})




    
    