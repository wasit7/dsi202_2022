# Generated by Django 2.2.5 on 2022-02-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
