# Generated by Django 3.1.7 on 2021-03-25 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0006_auto_20210320_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
            },
        ),
        migrations.CreateModel(
            name='PerfilViajante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.destino')),
            ],
            options={
                'verbose_name': 'perfilviajante',
                'verbose_name_plural': 'perfilviajantes',
            },
        ),
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo_viajante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.perfilviajante')),
            ],
            options={
                'verbose_name': 'passagem',
                'verbose_name_plural': 'passagems',
            },
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo_viajante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.perfilviajante')),
            ],
            options={
                'verbose_name': 'hospedagem',
                'verbose_name_plural': 'hospedagems',
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo_viajante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.perfilviajante')),
            ],
            options={
                'verbose_name': 'extra',
                'verbose_name_plural': 'extras',
            },
        ),
        migrations.CreateModel(
            name='Alimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tipo_viajante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.perfilviajante')),
            ],
            options={
                'verbose_name': 'alimentacao',
                'verbose_name_plural': 'alimentacaos',
            },
        ),
    ]