# Generated by Django 5.0 on 2023-12-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bolo_created_at_bolo_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolo',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
