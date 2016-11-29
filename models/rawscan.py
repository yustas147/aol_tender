# -*- coding: utf-8 -*-
from openerp import api, models, fields
from openerp.tools import logging
from yanp import nessus_parser

_mylog = logging.getLogger('yustas##########')

class rawscan_base(models.Model):
    _name = 'aol.rawscan.base'
    _inherits = {'ir.attachment':'att_id'}
#    type_of_scan = fields.Many2one(comodel_name='aol.scantype', string="Source of the scan")
    create_date = fields.Datetime(string='Created on:', readonly=True)
    body = fields.Text('Raw scan body')

    assets_ids = fields.Many2many(comodel_name='res.partner',relation='scans_assets')
    risk_ids = fields.One2many(comodel_name='crm.lead',inverse_name='rawscan_id')
    
    def raw_risk_create(self):
        # 
        pass
    
    @api.multi
    def get_att_location(self):
   #     _mylog.info('file path is: %s' % (unicode(self.att_id._full_path(self.att_id.store_fname))))
        return self.att_id._full_path(self.att_id.store_fname)
        
    @api.multi
    def parse_att(self):
        pass
#         file_loc = self.att_id._full_path(self.att_id.store_fname)
#         np = nessus_parser(file_loc)
#         res = np.print_org_format()
#         _mylog.info(unicode(res))
    
    @api.multi
    def procAsset(self, assetHost):
        envAsset = self.env['res.partner']
        instAsset = envAsset.search([('name','=',assetHost)])
#        instAsset = envAsset.search([('hostOrIp','==',assetHost)])
        if not len(instAsset):
            return envAsset.create({'name': assetHost, 'is_asset':True})
#            return envAsset.create({'hostOrIp': assetHost})
        return instAsset
    
    @api.multi
    def process_scanParseResults(self, **kwargs):
        #riskEnv = self.env['crm.lead']
        for host, risks in kwargs.iteritems():
            instAsset = self.procAsset(host)
            for risk in risks:
                r_inst = self.procRisk(asset=instAsset, risk=risk)
                if r_inst:
                    r_inst.create_attrs(**risk)
                
    @api.multi
    def procRisk(self, asset=None, risk=None):        
        envRisk = self.env['crm.lead']
      #  envRiskTypeValue = self.env['aol.attr.value']
        # need to implement check for existing risk
        def get_risk_name(risk):
            return unicode("Category: [%s] Descr: [%s] Severity: [%s]" % (risk['service_name'],risk['plugin_name'],risk['cvss']))
        
        risk_name = get_risk_name(risk)
        if not envRisk.search([('rawscan_id','=', self.id),('name','=',risk_name)]):
            return envRisk.create({'name': get_risk_name(risk), 'is_risk':True, 'partner_id':asset.id, 'description':unicode(risk), 'rawscan_id':self.id, })





class  rawscan_nessus(models.Model):
    _name = 'aol.rawscan.nessus'
    _inherits = {'aol.rawscan.base':'rawscan_base_id'}
    
    def parse_asset(self):
        # extracts asset data from records , creates risk records
        # returns risk rec id with raw body
        pass

    @api.multi
    def parse_att(self):
        file_loc = self.rawscan_base_id.get_att_location()
#        file_loc = self.rawscan_base_id.get_att_location(self.rawscan_base_id)
        np = nessus_parser(file_loc)
        res = np.print_org_format()
        return res
    
    @api.multi
    def risk_produce(self):
        #extracts risks from scan
        d_scan = self.parse_att()
        self.rawscan_base_id.process_scanParseResults(**d_scan)

class asset_type(models.Model):
    _name = 'aol.asset.type'
    
    name = fields.Char(string="Asset type")

class risk_type(models.Model):
    _name = 'aol.risk.type'
    
    name = fields.Char(string='Risk type')
    description = fields.Text(string='Short Description')
    risk_attr_ids = fields.Many2many(comodel_name='aol.attr', relation='risk_type_attr', 
                                      column1='rtype', 
                                      column2='attrib', 
                                      string='Risk attributes')
    risk_ids = fields.One2many(comodel_name='crm.lead', inverse_name='type_id', 
                              string='Risks (just for info)')
    
class attr_value(models.Model):
    _name = 'aol.attr.value'
    
    value = fields.Char(string='Value')
    attr_id = fields.Many2one(comodel_name='aol.attr', string='Custom Attribute')
    #type_id = fields.Many2one(comodel_name='aol.risk.type', string='Risk type value')
    risk_id = fields.Many2one(comodel_name='crm.lead', string='Risk', ondelete='cascade')
    
    
class attribute(models.Model):
    _name = 'aol.attr'
    
    name = fields.Char(string='Attribute')
    attr_value_ids = fields.One2many(comodel_name='aol.attr.value', inverse_name='attr_id', 
                                    string='Values (just for info)')
    risk_type_ids = fields.Many2many(comodel_name='aol.risk.type', relation='risk_type_attr', column1='attrib', column2='rtype', string='Risk types')
    
    

    
####Assume asset is res.partner
#class res_partner(models.Model):
##class asset_base(models.Model):
    #_inherit='res.partner'
##    _name='aol.asset.base'
    
