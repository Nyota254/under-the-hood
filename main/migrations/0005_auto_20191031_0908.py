# Generated by Django 2.2.6 on 2019-10-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191031_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='car_model_image',
            field=models.ImageField(blank=True, default='default_car_model.jpg', upload_to='car_model_images'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_image',
            field=models.ImageField(blank=True, default='default_car_part.jpg', upload_to='part_images'),
        ),
    ]
