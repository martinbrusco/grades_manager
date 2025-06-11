from odoo import models, fields

class Course(models.Model):
    _name = 'grades.manager.course'
    _description = 'Course'
    
    
    def _default_teacher_id(self):
        teacher = self.env['res_partner'].seach(
            [('is_teacher', '=', True), ('email', '=', 'mainteacher@gg.com')], limit=1)
        return teacher.id

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student Quantity')
    grade_average = fields.Float(string='Average Grade')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is Active')
    course_start = fields.Date(string='Course Start', default=fields.Date.today())
    course_end = fields.Date(string='Course End')
    last_evaluation_date = fields.Datetime(string='Last Evaluation')
    course_icon = fields.Binary(string='Course Icon')
    course_shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ], string='Course Shift')
    states = fields.Selection([
        ('register', 'Register'),
        ('in_progrest','In progrest'),
        ('finished','Finished')
    ], string='Course Shift', default= 'register')
    
    
    
    
    
    teacher_id = fields.Many2one(
        'res.partner',
        string='Teacher',
        ondelete='set null'
    )
    
    evaluation_ids = fields.One2many(
        'grades.manager.evaluation', 
        'course_id', 
        string='Evaluations'
    )
    
    student_ids = fields.Many2many(
        'res.partner', 
        'grades_course_student_rel',
        string = 'Student'
    )