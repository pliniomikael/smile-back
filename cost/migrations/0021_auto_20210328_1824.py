# Generated by Django 3.1.7 on 2021-03-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0020_auto_20210328_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumodate',
            name='money_month',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]
