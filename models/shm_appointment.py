from odoo import models, fields, api
class smart_hm_core(models.Model):
    _name = 'shm.appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'ref'
    _description = 'smart hospital management core'
     
    
    patient_id = fields.Many2one('shm.patient','Patient', tracking=True) 
    gender = fields.Selection(related='patient_id.gender',store= True)
    ref = fields.Char('Reference')
    booking_date  = fields.Date(
        string='Booking Date ',
        default=fields.Date.context_today,
    ) 
    appointment_time = fields.Datetime(
        string='Appointment Time',
        default=fields.Datetime.now,
    ) 
    description = fields.Html(
        string='Description',
        placeholder = "Describe your previous history"
    )
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    
    state = fields.Selection(
        string='state',
        selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'),('cancel', 'Cancel'),('done', 'Done'),]
    )
    
    def action_draft(self):
        self.state='draft'
    
    def action_in_consultation(self):
        self.state='in_consultation'
        
    def action_cancel(self):
        self.state='cancel'

    
    
    
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref
    
     
    
    
    
    