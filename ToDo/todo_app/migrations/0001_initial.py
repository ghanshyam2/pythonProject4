# Generated by Django 4.0 on 2023-04-24 05:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 4, 24, 5, 2, 2, 859357, tzinfo=utc))),
            ],
        ),
    ]