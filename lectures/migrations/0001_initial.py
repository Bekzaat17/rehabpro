# Generated by Django 5.2.1 on 2025-05-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('content', models.TextField(verbose_name='Содержание (HTML или Markdown)')),
                ('file', models.FileField(blank=True, null=True, upload_to='lectures/files/', verbose_name='Файл (PDF, DOC и т.д.)')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео (YouTube и т.п.)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекции',
            },
        ),
        migrations.CreateModel(
            name='LectureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория лекции',
                'verbose_name_plural': 'Категории лекций',
            },
        ),
    ]
