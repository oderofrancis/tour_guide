# Generated by Django 3.1.6 on 2021-02-17 06:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0008_auto_20210217_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None)),
                ('number_of_slots', models.PositiveIntegerField()),
                ('from_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('to_date', models.DateTimeField()),
                ('where_to_book', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
