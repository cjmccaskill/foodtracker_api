# Generated by Django 3.2.7 on 2021-09-08 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0002_tracker_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='quantity',
            new_name='servings',
        ),
    ]