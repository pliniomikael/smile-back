# Generated by Django 3.1.7 on 2021-03-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0002_auto_20210320_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='citie',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
