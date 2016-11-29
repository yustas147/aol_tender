from openerp.osv import osv
from openerp import api, models, fields
from datetime import datetime
from openerp import tools
import logging

_mylog = logging.getLogger('YUSTAS#################################################')

class res_partner(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
  
    is_asset = fields.Boolean(string='Is an asset')
    is_person = fields.Boolean(string='Is a person')
    risk_ids = fields.One2many(comodel_name='crm.lead', inverse_name='partner_id', 
                              string="Risks")
    asset_ids = fields.One2many(comodel_name="res.partner", inverse_name="manager_id", 
                               string="Assets Owned")
    manager_id = fields.Many2one(comodel_name="res.partner", string="Managed by")
    hostname = fields.Char(string="Hostname")
    ip_address = fields.Char(string="IpAddress")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    
    asset_type = fields.Many2one(comodel_name='aol.asset.type', string="Asset type")
    
    

    
    