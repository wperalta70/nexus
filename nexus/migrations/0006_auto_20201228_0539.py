# Generated by Django 3.1.4 on 2020-12-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0005_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('IN DEVELOPMENT', 'IN DEVELOPMENT'), ('IN PRODUCTION', 'IN PRODUCTION'), ('INACTIVE', 'INACTIVE')], max_length=14),
        ),
    ]
