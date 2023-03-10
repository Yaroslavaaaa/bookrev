# Generated by Django 4.1.6 on 2023-02-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_genre_id_books_genre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книги', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='books',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.IntegerField(),
        ),
    ]
