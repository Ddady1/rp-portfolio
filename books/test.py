from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("testh.html")

@app.route("/goudprijs")
def priceTracker():
    url = 'https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF'
    page = request.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class':'D(ib) Mend(20px)'})[0].find('fin-streamer').text
    return render_template('testh.html', price=price)