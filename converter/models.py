from django.db import models

class PlanFile(models.Model):
    pdf_file = models.FileField(upload_to='uploads/')
    svg_file = models.FileField(upload_to='converted/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
