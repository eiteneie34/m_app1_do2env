# Generated by Django 3.2.5 on 2021-10-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendulum_show', '0003_remove_penshow_video_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='penshow',
            name='video_t',
            field=models.FileField(blank=True, default='pendulum/anim_t', upload_to='pendulum'),
        ),
    ]
