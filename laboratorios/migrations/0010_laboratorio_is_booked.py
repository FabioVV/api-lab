# Generated by Django 4.2.4 on 2023-10-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0009_laboratorio_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
