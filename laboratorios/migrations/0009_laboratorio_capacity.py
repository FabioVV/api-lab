# Generated by Django 4.2.4 on 2023-10-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0008_alter_laboratorio_about_alter_laboratorio_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
