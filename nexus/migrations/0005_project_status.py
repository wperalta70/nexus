# Generated by Django 3.1.4 on 2020-12-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0004_auto_20201228_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('IN DEVELOPMENT', 'IN DEVELOPMENT'), ('IN PRODUCTION', 'IN PRODUCTION'), ('INACTIVE', 'INACTIVE')], default='IN DEVELOPMENT', max_length=14),
        ),
    ]
