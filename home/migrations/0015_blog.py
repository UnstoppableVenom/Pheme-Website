# Generated by Django 2.2.7 on 2022-06-18 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220618_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=200, unique=True)),
                ('blogAuthor', models.CharField(max_length=200)),
                ('blogContent', models.TextField(default=None)),
                ('blogCreatedOn', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-blogCreatedOn'],
            },
        ),
    ]
