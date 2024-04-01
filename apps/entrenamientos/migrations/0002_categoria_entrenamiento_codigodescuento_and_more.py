# Generated by Django 5.0 on 2024-04-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='codigoDescuento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='precioDescuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='categorias',
            field=models.ManyToManyField(related_name='entrenamientos', to='entrenamientos.categoria'),
        ),
    ]
