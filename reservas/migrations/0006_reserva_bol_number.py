# Generated by Django 4.2.4 on 2023-09-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_reserva_booked_at_reserva_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='bol_number',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
