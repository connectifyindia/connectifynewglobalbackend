# Generated by Django 4.2.1 on 2024-01-20 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='agreetoterms',
        ),
    ]