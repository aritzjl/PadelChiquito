# Generated by Django 4.2.7 on 2023-11-16 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comparador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('video_url', models.URLField()),
                ('plataforma', models.CharField(choices=[('INSTA', 'Instagram'), ('TIKTOK', 'TikTok'), ('YOUTUBE', 'YouTube')], max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('pala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comparador.pala')),
            ],
        ),
    ]
