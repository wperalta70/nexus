# Generated by Django 3.1.4 on 2021-01-13 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0013_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]