from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import yfinance as yf
import plotly.graph_objs as pgo
import plotly
import plotly.offline


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}

    return render(request, 'Registerpage.html', context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context={}

    return render(request, 'Loginpage.html',context)

def home(request):
    # Url and Request
    general_article_url = 'https://finance.yahoo.com/topic/stock-market-news/'
    general_article_r = requests.get(general_article_url)
    general_article_soup = BeautifulSoup(general_article_r.content, 'html.parser')
    # Pre-made Article lists
    article_titles = []
    article_links = []
    article_source = []
    # Finding the html of all the articles in the general stocks website and putting them on a list
    divs = general_article_soup.find_all('div', {'class': 'Py(14px) Pos(r)'})
    # Loop to get Info from article lists
    for div in divs:
        # Find indiviual article href link, article title, and source/time  (Note: source is html tags while others are text)
        anchor = div.find('a')
        title = div.find('h3')
        source = div.find('div', {'class': 'C(#959595) Fz(11px) D(ib) Mb(6px)'})
        # Adding indiviual article info to respective lists
        article_links.append(anchor['href'])
        article_titles.append(title.getText())
        article_source.append(source)
    zipped = zip(article_titles, article_links)

    context = {
       "name1":  "PYPL",
       "name2":  "AAPL",
       "name3":  "MSFT",
       "name4":  "AMZN",
       "name5":  "FB",
       "name6":  "TSLA",
       "name7":  "NVDA",
       "links":  article_links,
       "titles": article_titles,
       "sources": article_source,
       "zips": zipped
    }

    return render(request, 'Homepage.html', context)


def stock(request, stockticker):
    # Getting Stock Ticker information
    url = 'https://finance.yahoo.com/quote/' + stockticker + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    close = soup.find('span', {'data-reactid': '54'}).text
    marketcap = soup.find('td', {'data-reactid': '132'}).text
    open = soup.find('td', {'data-reactid': '100'}).text
    bid = soup.find('td', {'data-reactid': '104'}).text
    ask = soup.find('td', {'data-reactid': '108'}).text
    dayrange = soup.find('td', {'data-reactid': '112'}).text
    yearrange = soup.find('td', {'data-reactid': '116'}).text
    dayvolume = soup.find('fin-streamer', {'data-reactid': '121'}).text
    averagevolume = soup.find('td', {'data-reactid': '125'}).text

    # Stock News
    # Url and Request
    stock_article_url = 'https://finance.yahoo.com/quote/' + stockticker + '/'
    stock_article_r = requests.get(stock_article_url)
    stock_article_soup = BeautifulSoup(stock_article_r.content, 'html.parser')
    # Pre-made Article lists
    stock_titles = []
    stock_links = []
    stock_source = []
    # Finding the html of all the articles in the specific stock website and putting them on a list
    divs = stock_article_soup.find_all('div', {'class': 'Ov(h) Pend(44px) Pstart(25px)'})
    # Loop to get Info from article lists
    for div in divs:
        # Find indiviual article href link, article title, and source/time  (Note: source is html tags while others are text)
        anchor = div.find('a')
        title = div.find('h3')
        source = div.find('div', {'class': 'C(#959595) Fz(11px) D(ib) Mb(6px)'})
        # Adding indiviual article info to respective lists
        stock_links.append(anchor['href'])
        stock_titles.append(title.getText())
        stock_source.append(source)
    zips = zip(stock_titles, stock_links)

    # Stock Chart
    # Need Ticker,  Period, and Interval
    # yf.download(tickers=answer1, period=answer2, interval=answer3)

    # Log in to Chart Studio account API
    #chart_studio.tools.set_credentials_file(username='Isacc123', api_key='m17RL6zzqylDlCxh8uEt')

    data = yf.download(tickers='TSLA', period='1d', interval='1m')
    chart = pgo.Figure()
    #Candlestick
    chart.add_trace(pgo.Candlestick(x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name = 'market data',
        increasing_line_color='cyan',
        decreasing_line_color='gray',
    ))

    chart.update_layout(
        title = 'TSLA Price Live',
        yaxis_title='Stock Price'
    )

    chart.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=5, label="5m", step="minute", stepmode="backward"),
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="1h", step="hour", stepmode="todate"),
                dict(count=2, label="2h", step="hour", stepmode="backward"),
                dict(count=4, label="4h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    chart_html = plotly.offline.plot(chart, include_plotlyjs=False, output_type='div')
    #chart.write_html('/playground/templates/chart.html')

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
        "stock_links":  stock_links,
        "stock_titles": stock_titles,
        "stock_sources": stock_source,
        "stock_zips": zips,
        "chart": chart_html
    }
    return render(request, 'stockpage.html', context)

def news(request):

    return render(request, 'Newspage.html')
