# Generated by Django 4.0.5 on 2022-07-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstTitle', models.CharField(max_length=50)),
                ('secTitle', models.CharField(max_length=50)),
                ('paragraph', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discounted', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
