# Generated by Django 2.1.7 on 2019-05-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_auto_20190525_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='show_times',
            name='hall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.Halls'),
        ),
        migrations.RemoveField(
            model_name='shows',
            name='hall',
        ),
    ]
