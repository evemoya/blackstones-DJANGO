# Generated by Django 3.2.3 on 2021-06-15 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_auto_inc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('publicado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BS.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_auto_inc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('foto', models.ImageField(null=True, upload_to='productos')),
                ('publicado', models.BooleanField(default=False)),
                ('portada', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BS.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Peluquero',
            fields=[
                ('id_auto_inc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='peluqueros')),
                ('publicado', models.BooleanField(default=False)),
                ('Sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BS.sucursal')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BS.categoria')),
            ],
        ),
    ]
