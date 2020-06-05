# Generated by Django 3.0.6 on 2020-06-05 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('route_from', models.CharField(default='Nai', max_length=100)),
                ('route_to', models.CharField(default='Nai', max_length=100)),
                ('fare', models.CharField(default=0, max_length=100)),
                ('sacco_name', models.CharField(default='kenya', max_length=100)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
