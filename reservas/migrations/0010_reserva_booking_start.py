# Generated by Django 4.2.1 on 2023-11-01 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0009_reserva_booking_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='booking_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
