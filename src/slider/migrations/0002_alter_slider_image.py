# Generated by Django 4.2.3 on 2023-11-09 09:52

from django.db import migrations, models
import slider.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=slider.models.get_file_path, verbose_name='Image 1920x1080'),
        ),
    ]
