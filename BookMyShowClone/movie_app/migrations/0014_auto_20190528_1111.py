# Generated by Django 2.1.7 on 2019-05-28 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0013_auto_20190527_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bought_ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
