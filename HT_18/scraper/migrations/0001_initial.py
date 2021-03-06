# Generated by Django 3.1.7 on 2021-02-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='')),
                ('discription', models.TextField(default='None', max_length=1000)),
                ('name', models.TextField(default='Without name', max_length=50)),
                ('phone_number', models.TextField(default='Without number', max_length=50)),
            ],
        ),
    ]