# Generated by Django 2.0.2 on 2018-02-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_subtitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
