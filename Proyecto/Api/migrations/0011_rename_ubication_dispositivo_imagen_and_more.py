# Generated by Django 4.0.3 on 2022-06-29 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_remove_person_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivo',
            old_name='ubication',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='dispositivo',
            old_name='owner',
            new_name='propietario',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='Dispositivo',
            new_name='Dispo',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='hour',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='perrito',
            old_name='owner',
            new_name='dueño',
        ),
        migrations.RenameField(
            model_name='perrito',
            old_name='age',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='perrito',
            old_name='dog_name',
            new_name='nombre_perrito',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='last_feed',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_name',
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='ubicacion',
            field=models.CharField(default='Cocina', max_length=50),
        ),
        migrations.AddField(
            model_name='horario',
            name='mensaje',
            field=models.CharField(default='JAMPIOIIIIII', max_length=50),
        ),
        migrations.AddField(
            model_name='perrito',
            name='raza',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='perrito',
            name='ult_alimentacion',
            field=models.CharField(default='asd', max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_usuarios',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AlterField(
            model_name='horario',
            name='cantidad_comida',
            field=models.IntegerField(),
        ),
    ]