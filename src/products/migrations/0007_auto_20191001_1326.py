# Generated by Django 2.0.7 on 2019-10-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190930_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
