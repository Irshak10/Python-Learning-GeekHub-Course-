# Generated by Django 3.1.5 on 2021-01-25 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20210125_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 19, 18, 28, 774694, tzinfo=utc)),
        ),
    ]