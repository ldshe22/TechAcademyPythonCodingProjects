# Generated by Django 2.0.7 on 2019-05-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190505_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]