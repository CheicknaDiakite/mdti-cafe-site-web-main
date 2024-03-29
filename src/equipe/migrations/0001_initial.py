# Generated by Django 4.2.3 on 2023-09-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
                ('prenom', models.CharField(max_length=300, verbose_name='Prénom')),
                ('numero', models.CharField(max_length=20, verbose_name='Numéro de téléphone')),
                ('image', models.ImageField(upload_to='equipe/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, unique=True, verbose_name='Nom du poste')),
            ],
        ),
        migrations.CreateModel(
            name='ReseauSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_reseau', models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedIn', 'LinkedIn')], max_length=40)),
                ('url', models.URLField(max_length=300, unique=True)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipe.membre')),
            ],
        ),
        migrations.AddField(
            model_name='membre',
            name='poste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipe.poste', verbose_name='Le poste'),
        ),
    ]
