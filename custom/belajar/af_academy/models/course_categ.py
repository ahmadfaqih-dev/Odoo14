from odoo import fields, models

class CourseCateg(models.Model):
    _name = 'course.categ'
    _description = 'This is course category'

    name = fields.Char(
        string='Course Category',
        required=True,
        help='Fill course category'
    )

    description = fields.Text(
        string='Desccription categories'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    course_ids = fields.One2many(
        comodel_name='academy.course',
        inverse_name='category_id',
        string='Course',
        required=False)