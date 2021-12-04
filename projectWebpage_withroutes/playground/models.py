from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TRILLION = 1000000000000
#class User(models.Model):
#	email = models.CharField(max_length=30)
#	password = models.CharField(max_length=30)

class Stocks(models.Model):
	stock_name =  models.CharField(max_length=30)
	stock_ticker = models.CharField(max_length=30)
	stock_description = models.CharField(max_length=100)
	stock_pclose = models.FloatField()
	stock_open = models.FloatField()
	stock_bid = models.CharField(max_length=30)
	stock_ask = models.CharField(max_length=30)
	stock_volume = models.PositiveIntegerField()
	stock_avgvolume = models.PositiveBigIntegerField()
	stock_mcap = models.CharField(max_length=30)
	submission_date = models.DateField()

class Dict(models.Model):
	invest_word = models.CharField(max_length=100)
	invest_defn = models.CharField(max_length=255)

class News(models.Model):
	news_url = models.CharField(max_length=255)
	news_snip = models.CharField(max_length=255)
	news_date = models.DateField()
	news_author = models.CharField(max_length=100)
	news_img_url = models.CharField(max_length=255)

class User_pref(models.Model):
	email = models.ForeignKey(User, on_delete=models.CASCADE)
	user_stock_preferences = models.CharField(max_length=255)
