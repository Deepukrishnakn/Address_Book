# Generated by Django 4.1.2 on 2022-10-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('latitude', models.CharField(blank=True, default='0', max_length=255)),
                ('longitude', models.CharField(blank=True, default='0', max_length=255)),
            ],
        ),
    ]
