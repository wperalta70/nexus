from django import forms
from .models import *

class CreateProjectForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Título: ',
        max_length = 150
    )

    description = forms.CharField(
        label = 'Descripción: ',
        widget = forms.Textarea(
            attrs = {
                'rows': 3,
            }
        )
    )
    
    image = forms.ImageField(
        label = 'Imágen: ',
        widget = forms.FileInput(
            attrs = {
                'class': 'custom-file-input',
                'id': 'customFile'
            }
        )
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'image']