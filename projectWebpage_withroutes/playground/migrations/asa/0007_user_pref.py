# Generated by Django 3.2.8 on 2021-12-03 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_delete_user_pref'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_pref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.user')),
                ('user_stock_preferences', models.ManyToManyField(to='playground.Stocks')),
            ],
        ),
    ]
