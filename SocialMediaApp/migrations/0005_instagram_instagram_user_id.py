# Generated by Django 4.2.1 on 2023-10-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0004_instagram_fb_group_id_instagram_fb_page_access_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='instagram_user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
