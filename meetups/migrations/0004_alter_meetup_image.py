# Generated by Django 3.2.8 on 2021-10-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_alter_meetup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
