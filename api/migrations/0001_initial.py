# Generated by Django 4.2.6 on 2023-11-17 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=300)),
                ('numero_jugadores', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id_partido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_partido', models.DateField()),
                ('hora_partido', models.TimeField()),
                ('numero_goles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id_jugador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('ano_nacimiento', models.IntegerField()),
                ('posicion', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo_Partido',
            fields=[
                ('id_equipo_partido', models.AutoField(primary_key=True, serialize=False)),
                ('resultado', models.CharField(max_length=50)),
                ('goles_ganador', models.IntegerField()),
                ('goles_perdedor', models.IntegerField()),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.equipo')),
                ('id_partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.partido')),
            ],
        ),
    ]
