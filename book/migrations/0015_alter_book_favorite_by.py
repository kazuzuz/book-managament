# Generated by Django 4.2.5 on 2023-10-27 09:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0014_alter_book_image_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='favorite_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]