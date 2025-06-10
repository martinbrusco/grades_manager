from odoo import models, fields


class Evaluation(models.Model):
    _name = 'grades.manager.evaluation'
    _description = 'Evaluations'
    
    
    name = fields.Char(string = 'Name')
    date = fields.Date(string = 'Date')
    observations = fields.Text(string = 'Observations')
    
    course_id = fields.Many2one('grades.manager.course', string = 'Course')