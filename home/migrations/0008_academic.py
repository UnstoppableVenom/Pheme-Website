# Generated by Django 3.2.9 on 2022-06-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadsImg', models.ImageField(blank=True, upload_to='acads')),
                ('acadsHead', models.CharField(max_length=100)),
                ('acadsdesc', models.CharField(max_length=1000)),
            ],
        ),
    ]
