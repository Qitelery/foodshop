# Generated by Django 3.2 on 2021-04-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='food_items_images'),
        ),
    ]
