# -*- coding: utf-8 -*-
from openerp import api, models, fields

class rawscan_base(models.Model):
    _name = 'aol.rawscan.base'
    
# load_date = builtin automatic create_date field
#    type_of_scan = fields.Many2one(comodel_name='aol.scantype', string="Source of the scan")
    body = fields.Text('Raw scan body')
    
    def raw_risk_create(self):
        # 
        pass
    

#class scantype(models.Model):
#    _name = 'aol.scantype'


class  rawscan_nessus(models.Model):
    _name = 'aol.rawscan.nessus'
    _inherits = {'aol.rawscan_base':'rawscan_base_id'}
    
    def parse_asset(self):
        # extracts asset data from records , creates risk records
        # returns risk rec id with raw body
        pass

class crm_lead(models.Model):
###Assume risk is crm_lead
#class risk_base(models.Model):
    _inherit='crm.lead'
#    _name='aol.risk.base'
    
    rawscan_id = fields.Many2one(comodel_name='aol.rawscan.base', string='Origin scan')
###assum asset is res.partner
    asset_id = fields.Many2one(comodel_name='res.partner', string='Asset')
#    asset_id = fields.Many2one(comodel_name='aol.asset', string='Asset')
    type_id = fields.Many2one(comodel_name='aol.risk.type', string='Type of risk')

class risk_type(models.Model):
    _name = 'aol.risk.type'
    
###Assume asset is res.partner
class res_partner(models.Model):
#class asset_base(models.Model):
    _inherit='res.partner'
#    _name='aol.asset.base'
