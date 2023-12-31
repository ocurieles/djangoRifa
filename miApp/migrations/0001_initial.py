# Generated by Django 4.2.7 on 2023-12-03 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('telefono', models.IntegerField()),
                ('winner', models.BooleanField(default=False)),
                ('numero_sorteo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rifas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('descripcion', models.TextField()),
                ('numeros_disponibles', models.PositiveIntegerField()),
                ('numeros_vendidos', models.PositiveIntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('numero_compra', models.IntegerField()),
                ('codigo', models.CharField(max_length=100)),
                ('sorteado', models.BooleanField(default=False)),
                ('participante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participante_id', to='miApp.participante')),
                ('rifas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rifas', to='miApp.rifas')),
            ],
        ),
        migrations.CreateModel(
            name='Premios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='premio_imagenes')),
                ('rifas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miApp.rifas')),
            ],
        ),
    ]
