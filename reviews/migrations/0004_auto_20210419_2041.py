# Generated by Django 3.2 on 2021-04-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_at',
            field=models.DateTimeField(),
        ),
    ]
