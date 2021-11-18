# Generated by Django 3.2.8 on 2021-11-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=30)),
                ('stock_ticker', models.CharField(max_length=30)),
                ('stock_description', models.CharField(max_length=100)),
                ('stock_pclose', models.FloatField()),
                ('stock_open', models.FloatField()),
                ('stock_bid', models.CharField(max_length=30)),
                ('stock_ask', models.CharField(max_length=30)),
                ('stock_volume', models.PositiveIntegerField(max_length=30)),
                ('stock_avgvolume', models.PositiveBigIntegerField(max_length=30)),
                ('stock_mcap', models.CharField(max_length=30)),
                ('submission_date', models.DateField()),
            ],
        ),
    ]