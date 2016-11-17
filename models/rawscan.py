# -*- coding: utf-8 -*-
from openerp import api, models, fields
from openerp.tools import logging
from yanp import nessus_parser

_mylog = logging.getLogger('yustas##########')

class rawscan_base(models.Model):
    _name = 'aol.rawscan.base'
    _inherits = {'ir.attachment':'att_id'}
    
# load_date = builtin automatic create_date field
#    type_of_scan = fields.Many2one(comodel_name='aol.scantype', string="Source of the scan")
#    name = fields.Char(string='Scan data')
    create_date = fields.Datetime(string='Created on:', readonly=True)
    body = fields.Text('Raw scan body')


    #bin_body = fields.Binary('File of scan dump')
    #bin_body_att = fields.Many2one(string='Dump file', comodel_name='ir.attachment')
    
    def raw_risk_create(self):
        # 
        pass
    
    @api.multi
    def get_file_path(self):
        _mylog.info('file path is: %s' % (unicode(self.att_id._full_path(self.att_id.store_fname))))
        
    @api.multi
    def parse_att(self):
        file_loc = self.att_id._full_path(self.att_id.store_fname)
        np = nessus_parser(file_loc)
        res = np.print_org_format()
        _mylog.info(unicode(res))
        
    

#class scantype(models.Model):
#    _name = 'aol.scantype'


class  rawscan_nessus(models.Model):
    _name = 'aol.rawscan.nessus'
    _inherits = {'aol.rawscan.base':'rawscan_base_id'}
    
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
