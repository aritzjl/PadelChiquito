# Generated by Django 5.0 on 2024-05-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparador', '0015_alter_favorito_palas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pala',
            name='descuento',
            field=models.FloatField(blank=True, null=True),
        ),
    ]