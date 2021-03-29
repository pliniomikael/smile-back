# Generated by Django 3.1.7 on 2021-03-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0017_trip_milhas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumo',
            old_name='date_end',
            new_name='trip_date',
        ),
        migrations.AddField(
            model_name='resumo',
            name='income',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
