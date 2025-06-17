from odoo import models, fields

class Grade(models.Model):
    _name = 'grades.manager.grade'
    _description = 'Grades grade'

    student_id = fields.Many2one('res.partner', string='Student', domain=[('is_student', '=', True)], required=True)
    value = fields.Float(string='Value', required=True)
    date = fields.Date(string='Date', required=True, default= fields.Date.today())
    evaluation_id = fields.Many2one('grades.manager.evaluation', string='Evaluation', ondelete='cascade', required=True)