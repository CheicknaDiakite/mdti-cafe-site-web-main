# Generated by Django 4.2.3 on 2023-11-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_alter_categorie_image_alter_formation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='numero_telephone',
            field=models.CharField(max_length=30),
        ),
    ]
