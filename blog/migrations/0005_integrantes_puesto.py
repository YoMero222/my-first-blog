# Generated by Django 2.2.13 on 2020-06-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_integrantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrantes',
            name='puesto',
            field=models.CharField(default='', max_length=200),
        ),
    ]
