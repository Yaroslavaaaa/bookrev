# Generated by Django 4.1.6 on 2023-02-24 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_time_create_alter_books_time_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='books',
            name='time_update',
        ),
    ]
