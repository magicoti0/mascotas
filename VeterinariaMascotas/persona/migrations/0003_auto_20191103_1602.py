# Generated by Django 2.2.6 on 2019-11-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_animal_tipoanimal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.TextField()),
                ('observaciones', models.TextField()),
                ('diagnostico', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='idDueno',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaConsulta', models.DateField(verbose_name='Fecha Consulta')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Animal')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Consulta')),
            ],
        ),
    ]
