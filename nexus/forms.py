from django import forms
from django.forms.widgets import ClearableFileInput
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

# Custom clearable file input widget - used in Project Update Form
class CustomClearableFileInput(ClearableFileInput):
    initial_text = 'Imágen actual'
    input_text = 'Cambiar Imágen'
    clear_checkbox_label = '¿Borrar imágen actual?'
    template_name = 'widgets/customClearableFileInput.html'

# Update Project Form
class UpdateProjectForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Título: ',
        max_length = 150
    )

    short_description = forms.CharField(
        label = 'Descripción Breve: ',
        max_length = 50,
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
        label = 'Cambiar Imágen: ',
        required = False,
        widget = CustomClearableFileInput()
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

class CreateTicketForm(forms.ModelForm):
    PRIORITY_CHOICES = (
        ('BAJA', 'BAJA'),
        ('MEDIA', 'MEDIA'),
        ('ALTA', 'ALTA'),
    )

    TYPE_CHOICES = (
        ('FEATURE', 'FEATURE'),
        ('BUG', 'BUG'),
        ('DISEÑO', 'DISEÑO'),
    )

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

    priority = forms.ChoiceField(
        label = 'Prioridad: ',
        choices = PRIORITY_CHOICES
    )

    type = forms.ChoiceField(
        label = 'Tipo: ',
        choices = TYPE_CHOICES
    )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'type']

class UpdateTicketForm(forms.ModelForm):
    PRIORITY_CHOICES = (
        ('BAJA', 'BAJA'),
        ('MEDIA', 'MEDIA'),
        ('ALTA', 'ALTA'),
    )

    STATUS_CHOICES = (
        ('NUEVO', 'NUEVO'),
        ('ASIGNADO', 'ASIGNADO'),
        ('EN DESARROLLO', 'EN DESARROLLO'),
        ('CERRADO', 'CERRADO'),
    )

    TYPE_CHOICES = (
        ('FEATURE', 'FEATURE'),
        ('BUG', 'BUG'),
        ('DISEÑO', 'DISEÑO'),
    )

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

    priority = forms.ChoiceField(
        label = 'Prioridad: ',
        choices = PRIORITY_CHOICES
    )

    status = forms.ChoiceField(
        label = 'Estado: ',
        choices = STATUS_CHOICES
    )

    type = forms.ChoiceField(
        label = 'Tipo: ',
        choices = TYPE_CHOICES
    )

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'type']