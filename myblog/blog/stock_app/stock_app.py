#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')

ticker = str(input("Type in the ticker symbol for the stock you would like info on: "))
ticker = ticker.upper()
ticker = yf.Ticker(ticker)

# get stock info
# stock_info = ticker.info

# for key,value in stock_info.items():
#     print(key, ":", value)

if ticker.info['longName'] != None:
    company_name = ticker.info['longName']
    print(f"Company name : {company_name}")

    ticker_symbol = ticker.info['symbol']
    print(f"Ticker : {ticker_symbol}")

    if 'financialCurrency' in ticker.info:
        currency = ticker.info['financialCurrency']
        print(f"Currency : {currency}")
    if 'sector' in ticker.info:
        sector = ticker.info['sector']
        print(f"Sector : {sector}")

    summary = ticker.info['longBusinessSummary']
    print(f"About : {summary}")

    year_high = ticker.info['fiftyTwoWeekHigh']
    print(f"52 week high :  {year_high}")

    year_low = ticker.info['fiftyTwoWeekLow']
    print(f"52 week low : {year_low}")

    two_hundred_day_average = ticker.info['twoHundredDayAverage']
    print(f"200 day average : {two_hundred_day_average}")

    fifty_day_average = ticker.info['fiftyDayAverage']
    print(f"50 day average : {fifty_day_average}")

    previous_close = ticker.info['previousClose']
    print(f"Previous close : {previous_close}")

    last_open = ticker.info['regularMarketOpen']
    print(f"Previous open : {last_open}")

    year_change = ticker.info['52WeekChange']
    print(f"52 week change : {year_change}")

    print(ticker.recommendations)
    print(ticker.institutional_holders)
else:
    print("Ticker symbol is not valid please try again.")

# Dates can be entered in as period = "1mo", 3mo, 5d, 1d, 1y, 5y, max
# or a specific time can be selected start="2007-01-01", end="2010-01-10"
stock_history = ticker.history(period="5y")

df = stock_history

plt.figure()
# Here we can use Open and High below
plt.plot(df['Close'])
plt.ylabel('Price $')
plt.xlabel('Year')
plt.show()

# https://www.youtube.com/watch?v=9nB__kJio-M
# If we want multiple tickers being showed in the table data, go to the end of this video



