# Generated by Django 4.2.3 on 2023-11-09 09:52

from django.db import migrations, models
import emploi.models


class Migration(migrations.Migration):

    dependencies = [
        ('emploi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploi',
            name='image',
            field=models.ImageField(upload_to=emploi.models.get_file_path, verbose_name='Image 1200x700'),
        ),
    ]