from openerp.osv import osv
from openerp import api, models, fields
from datetime import datetime
from openerp import tools
import logging

_mylog = logging.getLogger('YUSTAS#################################################')

class res_partner(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
  
    is_asset = fields.Boolean(string='This is asset')
    
    