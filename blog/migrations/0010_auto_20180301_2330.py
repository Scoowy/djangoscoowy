# Generated by Django 2.0.2 on 2018-03-02 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180301_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='Fecha de creacion',
        ),
        migrations.AddField(
            model_name='comentario',
            name='fechaCreacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
