from odoo import models, fields


class Course(models.Model):
    _name = 'grades_manager'
    
    name = fields.Char(string='Name')
    studen_qty = fields.Integer(string='Studen quantity')   



    
