# Generated by Django 4.2.1 on 2023-11-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0010_reserva_booking_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='booking_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]