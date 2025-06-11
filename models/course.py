from odoo import models, fields, api

class Course(models.Model):
    _name = 'grades.manager.course'
    _description = 'Course'

    def _default_teacher_id(self):
        teacher = self.env['res.partner'].search(
            [('is_teacher', '=', True), ('email', '=', 'mainteacher@gg.com')],
            limit=1
        )
        return teacher.id if teacher else False

    name = fields.Char(string='Name', required=True)
    student_qty = fields.Integer(string='Student Quantity')
    grade_average = fields.Float(string='Average Grade')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is Active')
    course_start = fields.Date(
        string='Course Start',
        default=fields.Date.today
    )
    course_end = fields.Date(string='Course End')
    last_evaluation_date = fields.Datetime(string='Last Evaluation')
    course_icon = fields.Binary(string='Course Icon')
    course_shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ], string='Course Shift')
    states = fields.Selection([
        ('register', 'Register'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ], string='State', default='register')
    teacher_id = fields.Many2one(
        'res.partner',
        string='Teacher',
        default=_default_teacher_id,
        ondelete='restrict'
    )
    #SE TRAE UN CAMPO DE OTRO MODELO, 
    # si lo quieres hacer editable hay que poner readonly='0' en el form 
    # y agregar en el modelo store = True
    teacher_email= fields.Char(related='teacher_id.email')

    evaluation_ids = fields.One2many(
        'grades.manager.evaluation',
        'course_id',
        string='Evaluations'
    )

    student_ids = fields.Many2many(
        'res.partner',
        'grades_course_student_rel',
        string='Students'
    )
