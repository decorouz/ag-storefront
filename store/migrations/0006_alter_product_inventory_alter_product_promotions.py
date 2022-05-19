# Generated by Django 4.0.4 on 2022-05-19 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_collection_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.promotion'),
        ),
    ]
