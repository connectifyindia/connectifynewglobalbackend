# Generated by Django 4.2.1 on 2023-10-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0007_twiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linkedln',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('video_url', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(blank=True, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
                ('access_token', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedln_person_urn', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedln_group_urn', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]