# Generated by Django 4.0.4 on 2022-05-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=7, null=True),
        ),
    ]