# Generated by Django 4.0.3 on 2022-07-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0013_delete_usuario_rename_imagen_dispositivo_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perrito',
            name='foto',
            field=models.ImageField(blank=True, upload_to='perritos'),
        ),
    ]
