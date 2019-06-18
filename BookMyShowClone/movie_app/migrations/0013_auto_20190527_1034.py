# Generated by Django 2.1.7 on 2019-05-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_bought_ticket_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bought_ticket',
            name='total_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bought_ticket',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
