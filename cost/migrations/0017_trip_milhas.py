# Generated by Django 3.1.7 on 2021-03-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0016_trip_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='milhas',
            field=models.FloatField(null=True),
        ),
    ]