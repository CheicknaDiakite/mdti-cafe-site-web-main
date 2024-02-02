# Generated by Django 4.2.3 on 2023-09-07 10:22

from django.db import migrations, models
import slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('reference', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(upload_to=slider.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]