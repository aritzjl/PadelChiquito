# Generated by Django 5.0 on 2024-05-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContenidoPublicitario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_1', models.ImageField(blank=True, null=True, upload_to='publicidad')),
                ('inicio_2', models.ImageField(blank=True, null=True, upload_to='publicidad')),
                ('inicio_3', models.ImageField(blank=True, null=True, upload_to='publicidad')),
                ('filtros_1', models.ImageField(blank=True, null=True, upload_to='publicidad')),
                ('filtros_2', models.ImageField(blank=True, null=True, upload_to='publicidad')),
            ],
        ),
    ]
