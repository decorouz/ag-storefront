# Generated by Django 4.0.4 on 2022-05-18 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TagItem',
            new_name='TaggedItem',
        ),
    ]
