# Generated by Django 4.0.3 on 2022-06-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogImg', models.ImageField(blank=True, upload_to='static')),
                ('blogDate', models.DateTimeField(auto_now_add=True)),
                ('blogHref', models.CharField(max_length=100)),
                ('blogHeading', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='welcomemessage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
