from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
SERVICE_CHOICES = [
    ('B2B', 'B2B Lead Generation'),
    ('LLG', 'Linkedin Lead Generation'),
    ('BELBV', 'Bulk Email List building and Verification'),
    ('DEWR', 'Data Entry and Web Research'),
    ('REST', 'Real Estate Skip Tracing'),
]        
class LeadService(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    year_in_school = models.CharField(
        max_length=10,
        choices=SERVICE_CHOICES,
    )
    def __str__(self):
        return self.title    
