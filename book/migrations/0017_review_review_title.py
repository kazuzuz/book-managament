# Generated by Django 4.2.5 on 2023-12-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_title',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
