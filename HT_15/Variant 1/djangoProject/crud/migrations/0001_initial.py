# Generated by Django 3.1.5 on 2021-01-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Product without title', max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('discription', models.TextField(default='')),
                ('quantity', models.IntegerField(default=0)),
                ('activation', models.BooleanField(default=False)),
            ],
        ),
    ]
