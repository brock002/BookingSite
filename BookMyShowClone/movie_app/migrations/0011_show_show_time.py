# Generated by Django 2.1.7 on 2019-05-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_auto_20190525_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_time',
            field=models.DateTimeField(null=True),
        ),
    ]