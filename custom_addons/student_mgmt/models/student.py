from odoo import models, fields

class Student(models.Model):
    _name = 'student.mgmt.student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    parent_name = fields.Char(string="Parent's Name")
    address = fields.Text(string='Address')
    student_class = fields.Char(string='Class')
