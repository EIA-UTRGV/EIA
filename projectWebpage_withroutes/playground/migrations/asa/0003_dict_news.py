# Generated by Django 3.2.8 on 2021-11-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_date', models.DateField()),
                ('news_author', models.CharField(max_length=100)),
            ],
        ),
    ]
