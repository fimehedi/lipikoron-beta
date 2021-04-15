# Generated by Django 3.1 on 2021-04-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_withdraw_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]