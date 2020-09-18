from django import forms
from .models import ProfileMer

class UploadForm(forms.ModelForm):
    class Meta:
        model = ProfileMer
        fields = {'title', 'photo'}