# Generated by Django 3.1.7 on 2021-03-27 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0007_alimentacao_destino_extra_hospedagem_passagem_perfilviajante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospedagem', models.DecimalField(decimal_places=2, max_digits=6)),
                ('alimentacao', models.DecimalField(decimal_places=2, max_digits=6)),
                ('extra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('passagem', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trip',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='cite',
        ),
        migrations.RemoveField(
            model_name='extra',
            name='tipo_viajante',
        ),
        migrations.RemoveField(
            model_name='hospedagem',
            name='tipo_viajante',
        ),
        migrations.RemoveField(
            model_name='passagem',
            name='tipo_viajante',
        ),
        migrations.RemoveField(
            model_name='perfilviajante',
            name='destino',
        ),
        migrations.DeleteModel(
            name='Alimentacao',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Citie',
        ),
        migrations.DeleteModel(
            name='Destino',
        ),
        migrations.DeleteModel(
            name='Extra',
        ),
        migrations.DeleteModel(
            name='Hospedagem',
        ),
        migrations.DeleteModel(
            name='Passagem',
        ),
        migrations.AddField(
            model_name='trip',
            name='tipo_viajante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.perfilviajante'),
        ),
    ]
