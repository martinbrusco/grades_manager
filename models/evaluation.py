from odoo import models, fields

class Evaluation(models.Model):
    _name = 'grades.manager.evaluation'
    _description = 'Evaluations'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    observations = fields.Text(string='Observations')
    course_id = fields.Many2one('grades.manager.course', string='Course', ondelete='cascade', required=True)
    grades_ids = fields.One2many('grades.manager.grade', 'evaluation_id', string='Grades')