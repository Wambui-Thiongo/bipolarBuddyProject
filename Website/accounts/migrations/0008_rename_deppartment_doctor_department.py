# Generated by Django 5.0.6 on 2024-08-01 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_departments_doctor_deppartment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='deppartment',
            new_name='department',
        ),
    ]
