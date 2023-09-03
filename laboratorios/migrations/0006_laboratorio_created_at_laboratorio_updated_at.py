# Generated by Django 4.2.1 on 2023-09-03 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0005_alter_laboratorio_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
