# Generated by Django 4.2.13 on 2024-06-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0008_carro_imagen_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('rut', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=50)),
                ('nacimiento', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=300)),
                ('contraseña', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(default='Images/juego6.jpg', upload_to='Images/'),
        ),
    ]
