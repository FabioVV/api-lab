# Generated by Django 4.2.4 on 2023-10-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_usuario_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]
