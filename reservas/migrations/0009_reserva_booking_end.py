# Generated by Django 4.2.1 on 2023-10-20 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0008_alter_reserva_laboratory'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='booking_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
