# Generated by Django 4.2.5 on 2023-09-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_review_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_text',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
