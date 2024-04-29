# Generated by Django 5.0 on 2024-04-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categorias',
            field=models.ManyToManyField(to='blog.categoria'),
        ),
    ]
