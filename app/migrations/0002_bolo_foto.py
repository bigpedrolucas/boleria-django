# Generated by Django 5.0 on 2023-12-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolo',
            name='foto',
            field=models.ImageField(null=True, upload_to='bolos_fotos/'),
        ),
    ]