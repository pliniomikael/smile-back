# Generated by Django 3.1.7 on 2021-03-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0013_resumodate'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumo',
            name='trip_cost',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='resumodate',
            name='trip_cost',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
