# Generated by Django 2.2.5 on 2022-01-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220120_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Car'),
        ),
        migrations.AddField(
            model_name='rent',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Client'),
        ),
    ]
