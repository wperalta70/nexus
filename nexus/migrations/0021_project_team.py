# Generated by Django 3.1.4 on 2021-04-02 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nexus', '0020_auto_20210220_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(related_name='team', to=settings.AUTH_USER_MODEL),
        ),
    ]