# Generated by Django 4.2.7 on 2023-11-16 11:35

import apps.comparador.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparador', '0006_tienda_preciopala'),
    ]

    operations = [
        migrations.AddField(
            model_name='pala',
            name='palaID',
            field=models.CharField(default=apps.comparador.models.generate_random_number, editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pala',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
