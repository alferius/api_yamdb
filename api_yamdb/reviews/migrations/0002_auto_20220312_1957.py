# Generated by Django 2.2.16 on 2022-03-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(choices=[('Books', 'Книги'), ('Films', 'Фильмы'), ('Music', 'Музыка')], unique=True, verbose_name='Уникальный адрес категории'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(choices=[('Fairytale', 'Сказка'), ('Rock', 'Рок'), ('ArtHouse', 'Артхаус'), ('Comedy', 'Комедия'), ('Thriller', 'Триллер'), ('Fantasy', 'Фантастика'), ('Classic', 'Классика'), ('Detective', 'Детектив'), ('Horrors', 'Ужасы'), ('Pop', 'Поп'), ('Chanson', 'Шансон')], unique=True, verbose_name='Уникальный адрес жанра'),
        ),
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(help_text='Введите текст поста', null=True, verbose_name='Рейтинг поста'),
        ),
    ]
