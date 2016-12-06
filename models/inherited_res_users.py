from openerp.osv import osv
from openerp import api, models, fields
from datetime import datetime
from openerp import tools
import logging

_mylog = logging.getLogger('YUSTAS####')

class res_users(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.users'
  
    is_asset = fields.Boolean(string='Is an asset')
    is_person = fields.Boolean(string='Is a person')
    
    risk_ids = fields.One2many(comodel_name='crm.lead', inverse_name='a_user_id', 
                              string="Risks")
    risk_count = fields.Integer(string="Risk Count", compute="_get_risk_count")
    
    @api.one
    @api.depends('risk_ids')
    def _get_risk_count(self):
        _mylog.info('self.id, name: %s # %s' % (unicode(self.id),unicode(self.name)))
        res = len(self.risk_ids)
        self.risk_count = res
        return res
    
    

    
    