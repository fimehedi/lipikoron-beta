# Generated by Django 3.1 on 2021-04-15 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_feature_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature_post',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
    ]