# Generated by Django 4.2.13 on 2024-06-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0023_remove_usuariofalso_tipousuario_delete_usuarioactual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='consola',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tipousuario',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
