# Generated by Django 3.2.5 on 2021-10-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendulum_show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='penshow',
            name='video_t',
            field=models.FileField(blank=True, default='pendulum/anim_t', upload_to='pendulum'),
        ),
        migrations.AddField(
            model_name='penshow',
            name='video_x',
            field=models.FileField(blank=True, default='pendulum/anim_x', upload_to='pendulum'),
        ),
    ]
