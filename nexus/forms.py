from django import forms
from .models import *

class CreateProjectForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Título: ',
        max_length = 150
    )

    short_description = forms.CharField(
        label = 'Descripción Breve: ',
        max_length = 150,
        required = False
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
        required = False,
        widget = forms.FileInput(
            attrs = {
                'class': 'custom-file-input',
                'id': 'customFile'
            }
        )
    )

    STATUS_CHOICES = (
        ('', '...'),
        ('EN DESARROLLO', 'EN DESARROLLO'),
        ('EN PRODUCCIÓN', 'EN PRODUCCIÓN'),
        ('INACTIVO', 'INACTIVO'),
    )

    status = forms.ChoiceField(
        label = 'Estado: ',
        choices = STATUS_CHOICES,
    )

    class Meta:
        model = Project
        fields = ['title', 'short_description', 'description', 'image', 'status']