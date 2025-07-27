from django import forms
from .models import PlanFile

class PlanUploadForm(forms.ModelForm):
    class Meta:
        model = PlanFile
        fields = ['pdf_file']
