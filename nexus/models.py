from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify


def get_upload_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'project_thumbnails/{0}/{1}'.format(self.slug, filename)


# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = (
        ('EN DESARROLLO', 'EN DESARROLLO'),
        ('EN PRODUCCIÓN', 'EN PRODUCCIÓN'),
        ('INACTIVO', 'INACTIVO'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 150)
    short_description = models.CharField(max_length = 150, null = True, blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_upload_path, blank = True, null = True, default = None)
    status = models.CharField(max_length = 14, choices = STATUS_CHOICES)
    date_created = models.DateTimeField(default = timezone.now)

    # Create a slug based on the project's title -> project-name
    slug = models.SlugField(max_length = 30, blank=True)

    def __str__(self):
        return f'Project: {self.title}'

    def save(self, *args, **kwargs):
        # Before saving, this line creates the slug based on the project's title
        self.slug = slugify(self.title)
        super().save()

        # These lines check if the project's thumbnail has a size greater than 300x300,
        # and if so resizes and re-saves it to the same path
        '''img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''
