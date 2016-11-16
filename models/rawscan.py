# -*- coding: utf-8 -*-

from openerp import api, models, fields

class rawscan(models.Model):
    _name = 'aol.rawscan'
    
# load_date = builtin automatic create_date field
    type_of_scan = fields.Many2one(comodel_name='aol.scantype', string="Source of the scan")
    body = fields.Text('Raw scan body')
    

