# Generated by Django 4.1.2 on 2022-10-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_alter_address_options_alter_address_latitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
    ]
