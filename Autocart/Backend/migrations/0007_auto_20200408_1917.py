# Generated by Django 3.0.5 on 2020-04-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_carimage_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='img',
            field=models.ImageField(upload_to='cars/'),
        ),
    ]
