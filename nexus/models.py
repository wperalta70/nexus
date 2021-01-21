from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify

# Function to get the project thumbnail upload path, using the project's title as a slug
def get_upload_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/project_thumbnails/<project-name>/<filename>
    return 'project_thumbnails/{project_name}/{filename}'.format(project_name = self.slug, filename = filename)


# Projects
class Project(models.Model):
    STATUS_CHOICES = (
        ('EN DESARROLLO', 'EN DESARROLLO'),
        ('EN PRODUCCIÓN', 'EN PRODUCCIÓN'),
        ('INACTIVO', 'INACTIVO'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'projects')
    title = models.CharField(max_length = 150)
    short_description = models.CharField(max_length = 50, null = True, blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_upload_path, blank = True, null = True, default = None)
    status = models.CharField(max_length = 14, choices = STATUS_CHOICES)
    date_created = models.DateTimeField(default = timezone.now)
    last_updated = models.DateTimeField(null = True, blank = True)

    # Create a slug based on the project's title -> project-name
    slug = models.SlugField(max_length = 30, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Before saving, this line creates the slug based on the project's title
        self.slug = slugify(self.title)
        super().save()

        # These lines check if the project's thumbnail has a size greater than 300x300,
        # and if so resizes to save space, and re-saves it to the same path
        '''img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''


# Tickets
class Ticket(models.Model):
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

    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'tickets')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'tickets')
    assigned_to = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='assigned_to', blank = True, null = True)
    title = models.CharField(max_length = 150)
    description = models.TextField()
    priority = models.CharField(max_length = 5, choices = PRIORITY_CHOICES)
    status = models.CharField(max_length = 13, choices = STATUS_CHOICES, default="NUEVO")
    type = models.CharField(max_length = 7, choices = TYPE_CHOICES)
    date_created = models.DateTimeField(default = timezone.now)
    date_closed = models.DateTimeField(null = True, blank = True)
    last_updated = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title

# Ticket comments
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    comment = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.comment

# Function to get the ticket's files upload path, using the project's title as a slug,
def get_ticket_file_upload_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/ticket_files/<ticket_id>/<filename>
    return 'ticket_files/ticket_{id}/{filename}'.format(id = self.ticket_id, filename = filename)

# Ticket files
class TicketFile(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE, related_name = 'ticketfiles')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'ticketfiles')
    title = models.CharField(max_length = 100)
    file = models.FileField(upload_to = get_ticket_file_upload_path)
    date_uploaded = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
