# Generated by Django 2.2.13 on 2020-06-25 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_integrantes_puesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='correo',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
