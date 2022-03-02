# Generated by Django 2.2.16 on 2022-03-01 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальный адрес категории')),
            ],
            options={
                'verbose_name': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование жанра')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальный адрес жанра')),
            ],
            options={
                'verbose_name': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название произведения')),
                ('year', models.IntegerField(max_length=4, verbose_name='Год выпуска')),
                ('rating', models.TextField(help_text='Введите текст поста', verbose_name='Текст поста')),
                ('description', models.TextField(blank=True, help_text='Введите текст поста', null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.Categories', verbose_name='Категория')),
                ('genre', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='api.Genres', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Titles',
            },
        ),
    ]
