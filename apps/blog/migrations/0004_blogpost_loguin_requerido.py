# Generated by Django 5.0 on 2024-04-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_portada_delete_visitablog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='loguin_requerido',
            field=models.BooleanField(default=False),
        ),
    ]
