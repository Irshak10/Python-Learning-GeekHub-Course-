# Generated by Django 3.1.5 on 2021-01-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
