# Generated by Django 4.0.2 on 2022-03-24 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_tile_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_item',
            old_name='quntity',
            new_name='quantity',
        ),
    ]
