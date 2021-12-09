from django.core.management.base import BaseCommand
from playground.models import User, Stocks
from datetime import date

class Command(BaseCommand):

	def handle(self, *args, **options):
		create_user("user1","password")
		create_stock("Johnson & Johnson",
			"JnJ",
			"makes apple phones every year",
			147.87,
			148.24,
			"0.00 x 1100",
			"0.00 x 1200",
			40264924,
			76143410,
			"2.426T",
			date.today()
			)

def create_user(email,password):
	user = User.objects.filter(email=email).first()
	if user is None:
		new_user = User()
		new_user.email = email
		new_user.password = password
		new_user.save()
	#print(user)

def create_stock(name,ticker,description,pclose,open,bid,ask,volume,avgvolume,mcap,sdate):
	new_stock = Stocks.objects.filter(stock_ticker = ticker).first()
	if ticker is None:
		new_stock = Stocks()
		new_stock.stock_name = name
		new_stock.stock_ticker = ticker
		new_stock.stock_description = description
		new_stock.stock_pclose = pclose
		new_stock.stock_open = open
		new_stock.stock_bid = bid
		new_stock.stock_ask = ask
		new_stock.stock_volume = volume
		new_stock.stock_avgvolume = avgvolume
		new_stock.stock_mcap = mcap
		new_stock.submission_date = sdate
		new_stock.save()
		#print(new_stock)
