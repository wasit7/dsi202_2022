# Generated by Django 2.2.5 on 2022-01-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(auto_now=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]