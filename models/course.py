from odoo import models, fields

class Course(models.Model):
    _name = 'grades.manager.course'
    _description = 'Course'

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student Quantity')   
    grade_average = fields.Float(string='Average Grade')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is Active')
    course_start = fields.Date(string='Course Start')
    course_end = fields.Date(string='Course End')
    last_evaluation_date = fields.Datetime(string='Last Evaluation')
    course_icon = fields.Binary(string='Course Icon')
    course_shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ], string='Course Shift')
