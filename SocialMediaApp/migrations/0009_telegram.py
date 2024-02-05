# Generated by Django 4.2.1 on 2023-10-26 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0008_linkedln'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('video_url', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(blank=True, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
                ('chat_id', models.CharField(blank=True, max_length=100, null=True)),
                ('bot_token', models.CharField(blank=True, max_length=500, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
