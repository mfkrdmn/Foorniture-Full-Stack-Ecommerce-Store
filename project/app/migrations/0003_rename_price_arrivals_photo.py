# Generated by Django 4.0.5 on 2022-07-04 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_arrivals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivals',
            old_name='price',
            new_name='photo',
        ),
    ]
