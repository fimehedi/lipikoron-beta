# Generated by Django 3.1.7 on 2021-04-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_lipikar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
