# Generated by Django 3.2.5 on 2021-11-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendulum_show', '0007_auto_20211110_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='penshow',
            name='mk_animv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='penshow',
            name='mk_animx',
            field=models.BooleanField(default=False),
        ),
    ]
