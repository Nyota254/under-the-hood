# Generated by Django 2.2.6 on 2019-11-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_car_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_type',
            name='car_type_logo',
            field=models.ImageField(default='default_logo.jpg', upload_to='car_type_logos'),
        ),
    ]
