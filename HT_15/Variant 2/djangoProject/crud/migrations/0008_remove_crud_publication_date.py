# Generated by Django 3.1.5 on 2021-01-31 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20210125_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crud',
            name='publication_date',
        ),
    ]