from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_teacher = fields.Boolean(string='Is Teacher')