# Generated by Django 5.0 on 2024-06-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparador', '0016_pala_descuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada_mas_antigua', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
