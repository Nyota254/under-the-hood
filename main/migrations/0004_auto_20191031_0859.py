# Generated by Django 2.2.6 on 2019-10-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191031_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_model',
            name='car_model_image',
            field=models.ImageField(blank=True, upload_to='car_model_images'),
        ),
        migrations.AddField(
            model_name='part',
            name='part_image',
            field=models.ImageField(blank=True, upload_to='part_images'),
        ),
    ]
