# Generated by Django 4.2.3 on 2023-09-07 10:22

from django.db import migrations, models
import django.db.models.deletion
import formation.models
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to=formation.models.get_file_path)),
                ('description', models.TextField(default='', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to=formation.models.get_file_path)),
                ('description', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation')),
            ],
        ),
    ]
