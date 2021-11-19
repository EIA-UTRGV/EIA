from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}


#    if request.method == 'POST':
#        return redirect(login)

    return render(request, 'Registerpage.html', context)

def login(request):

    if request.method == 'POST':
        return redirect(home)

    return render(request, 'Loginpage.html')

def home(request):
    context = {
       "name2":  "AAPL",
       "name3":  "MSFT",
       "name4":  "AMZN",
       "name5":  "FB",
       "name6":  "TSLA",
       "name7":  "NVDA"
    }

    return render(request, 'Homepage.html', context)

def stock(request, stockticker):
    url = 'https://finance.yahoo.com/quote/' + stockticker + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    close = soup.find('span', {'data-reactid': '52'}).text
    marketcap = soup.find('span', {'data-reactid': '138'}).text
    open = soup.find('span', {'data-reactid': '102'}).text
    bid = soup.find('span', {'data-reactid': '107'}).text
    ask = soup.find('span', {'data-reactid': '112'}).text
    dayrange = soup.find('td', {'data-reactid': '116'}).text
    yearrange = soup.find('td', {'data-reactid': '120'}).text
    dayvolume = soup.find('span', {'data-reactid': '125'}).text
    averagevolume = soup.find('td', {'data-reactid': '129'}).text

    context = {
        "stockname": name,
        "stockprice": price,
        "stockclose": close,
        "stockopen": open,
        "stockbid": bid,
        "stockask": ask,
        "stockdayrange": dayrange,
        "stockyearrange": yearrange,
        "stockdayvolume" : dayvolume,
        "stockaveragevolume": averagevolume,

        "stockmarketcap": marketcap,
    }
    return render(request, 'stockpage.html', context)

def news(request):

    return render(request, 'Newspage.html')
