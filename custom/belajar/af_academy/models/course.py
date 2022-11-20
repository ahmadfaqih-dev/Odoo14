from odoo import fields, models

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char(
        string='Course Name',
        required=True,
        help="Fill course name"
    )

    description = fields.Text(
        string='This is Description',
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    category_id = fields.Many2one(
        comodel_name='course.categ',
        string='Category',
        required=False
    )