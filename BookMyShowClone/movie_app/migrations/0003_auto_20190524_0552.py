# Generated by Django 2.1.7 on 2019-05-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20190524_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halls',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]