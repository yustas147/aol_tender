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
    
    risk_ids = fields.One2many(comodel_name='crm.lead', inverse_name='user_id', 
                              string="Risks")
    #risk_cnt = fields.Integer(string="Risk Count", compute=)
    risk_cnt = fields.Integer(string="Risk Count", compute="_get_risk_count")
    
    @api.one
    def _get_risk_count(self):
        #_mylog.info('self.id, name: %s # %s' % (unicode(self.id),unicode(self.name)))
        #envRisk = self.env['crm.lead']
        #risks = envRisk.search([('user_id.id','=',self.id)])
        res = len(self.risk_ids)
        self.risk_cnt = res
        return res
    
    @api.one
    def get_risk_cnt(self):
        #_mylog.info('self.id, name: %s # %s' % (unicode(self.id),unicode(self.name)))
        print "PIZDETS!!!!"
        envRisk = self.env['crm.lead']
        risks = envRisk.search([('user_id.id','=',self.id)])
        res = len(risks)
        self.risk_cnt = res
        _mylog.info('res is: %s ' % (unicode(res)))
        return res    
    
    

    
    