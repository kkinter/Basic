# Generated by Django 3.2.13 on 2022-10-05 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_feautre_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='feautre_image',
            new_name='featured_image',
        ),
    ]
