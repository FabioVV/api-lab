# Generated by Django 4.2.1 on 2023-08-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0004_laboratorio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
