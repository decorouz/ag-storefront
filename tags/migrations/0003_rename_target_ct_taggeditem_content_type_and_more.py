# Generated by Django 4.0.4 on 2022-05-19 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_rename_tagitem_taggeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggeditem',
            old_name='target_ct',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='taggeditem',
            old_name='target_id',
            new_name='object_id',
        ),
    ]
