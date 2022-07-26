# Generated by Django 4.0.5 on 2022-07-19 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('nacionalidad', models.CharField(choices=[('ecuatoriana', 'ecuatoriana'), ('peruana', 'peruana'), ('colombiana', 'colombiana')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=100)),
                ('numero_cuartos', models.IntegerField()),
                ('valor_alicuota', models.DecimalField(decimal_places=2, max_digits=100)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losdepartamentos', to='administrativo.propietario')),
            ],
        ),
    ]
