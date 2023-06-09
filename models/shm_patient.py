# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
class smart_hm_core(models.Model):
    _name = 'shm.patient'
    _description = 'smart hospital management core'

    name = fields.Char('Name')
    ref = fields.Char('Reference') 
    image = fields.Image('Image')
    gender = fields.Selection(
        string='Sex',
        selection=[('male', 'Male'), ('female', 'Female')]
    ) 
    date_of_birth = fields.Date(
        string='Date of Birth',
        default=fields.Date.context_today,
    ) 
    active = fields.Boolean(
        string='Is Active ?',
        default=True
        
    ) 
    appointment_id = fields.Many2one(
        string='Appointments',
        comodel_name='shm.appointment',
        ondelete='restrict',
    )
    
    age = fields.Integer(
        string='Age', compute='_compute_age', store=True)
    
    phone = fields.Char('Contact')
     
    emergency_contact = fields.Char(
        string='Emergency Contact',
    ) 
    
    blood_group = fields.Selection(
        string='Blood Group',
        selection=[('o+', 'O+'),('o-', 'O-'), ('a-', 'A-'),('a+', 'A+'),('b-', 'B-'),('b+', 'B+'),('ab-', 'AB-'),('ab+', 'AB+'),]
    )
     
    history = fields.Text(
        string='history',
    ) 
 

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.date_of_birth:
                delta = relativedelta(today, record.date_of_birth)
                record.age = delta.years
            else:
                record.age = 0
    
