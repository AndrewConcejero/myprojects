# Generated by Django 3.0.8 on 2020-08-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISworkshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepage',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes'),
        ),
    ]