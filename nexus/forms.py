from django import forms
from django.forms.widgets import ClearableFileInput, PasswordInput, TextInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

### PROJECT FORMS ###

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

### PROJECT FORMS ###




### TICKET FORMS ###

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

### TICKET FORMS ###





### TICKET COMMENT FORMS ###

# Custom input group widget - used in Create Comment Form (for tickets)
class CustomCommentInput(TextInput):
    template_name = 'widgets/customCommentInput.html'

class CreateCommentForm(forms.ModelForm):
    comment = forms.CharField(
        required = True,
        max_length = 255,
        widget = CustomCommentInput(),
        label = False
    )

    class Meta:
        model = Comment
        fields = ['comment']

### TICKET COMMENT FORMS ###


### TICKET FILE FORMS ###

class TicketFileUploadForm(forms.ModelForm):
    title = forms.CharField(
        required = True,
        max_length = 100,
        label = 'Título:'
    )

    file = forms.FileField(
        required = True,
        widget = forms.FileInput(
            attrs = {
                'class': 'custom-file-input',
                'id': 'customFile'
            }
        ),
        label = 'Archivo:',
    )

    class Meta:
        model = TicketFile
        fields = ['title', 'file']

### TICKET FILE FORMS ###

### USER FORMS ###

USER_ROLES = (
    ('', '...'),
    ('admin', 'Administrador'),
    ('developer', 'Desarrollador'),
    ('project_manager', 'Project Manager'),
    ('tester', 'Tester'),
)

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    first_name = forms.CharField(
        required = True,
        label = 'Nombre',
        max_length = 150
    )

    last_name = forms.CharField(
        required = True,
        label = 'Apellido',
        max_length = 150
    )

    email = forms.EmailField(
        required = True,
        label = 'Dirección de email',
    )

    role = forms.ChoiceField(
        required = True,
        label = 'Tipo de usuario',
        choices = USER_ROLES
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        required = True,
        label = 'Dirección de email',
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(
        label = 'Cambiar Imágen: ',
        required = False,
        widget = CustomClearableFileInput()
    )

    class Meta:
        model = Profile
        fields = ['image']

### USER FORMS ###