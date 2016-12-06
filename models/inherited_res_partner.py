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
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
#    asset_type = fields.Many2one(comodel_name='aol.asset.type', string="Asset type")
    severity_rating = fields.Integer(string="Severity Rating", help="Factor of severeness of risks for this asset. Computed or set manually")
    parent_id = fields.Many2one(comodel_name='res.partner', string="Parent Asset")
    asset_date = fields.Datetime(string="Register date")
    asset_type = fields.Selection(selection=[('website','Website'),('server','Server'),
                                             ('product','Product'),('software','Software')], string='Asset Type')
    server_ip_address = fields.Char(string="IpAddress")
    server_os = fields.Char(string="OS")
    server_os_version = fields.Char(string="OS version")
    website_hostname = fields.Char(string="Hostname")
    product_name = fields.Char(string="Product Name")
    software_name = fields.Char(string="Software Name")
    psw_description = fields.Text(string="Description")
    decommissioned = fields.Boolean(string="Decommissioned in 3 month")
    
    
    

    
    