# Generated by Django 2.2.13 on 2020-06-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_imagenengaleria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
