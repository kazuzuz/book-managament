# Generated by Django 4.2.5 on 2023-10-02 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_remove_book_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorite_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='お気に入りの本'),
        ),
    ]