# Generated by Django 5.0 on 2024-06-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpost_fotoautor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='fotoAutor',
            field=models.ImageField(blank=True, null=True, upload_to='autor/'),
        ),
    ]
