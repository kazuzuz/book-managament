# Generated by Django 4.2.5 on 2023-10-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_account_favorite_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='favorite_book',
        ),
    ]
