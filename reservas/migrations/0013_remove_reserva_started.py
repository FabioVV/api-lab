# Generated by Django 4.2.1 on 2023-11-10 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0012_reserva_started'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='started',
        ),
    ]
