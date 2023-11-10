# Generated by Django 4.2.2 on 2023-11-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_genre_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('HORROR', 'horror'), ('COMEDY', 'comedy'), ('ROMANCE', 'romance'), ('ACTION', 'action'), ('SCI-FI', 'sci-fi'), ('SCIENCE', 'science')], default=1, max_length=20, verbose_name='genre of this book'),
            preserve_default=False,
        ),
    ]
