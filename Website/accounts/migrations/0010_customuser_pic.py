# Generated by Django 5.0.6 on 2024-08-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]