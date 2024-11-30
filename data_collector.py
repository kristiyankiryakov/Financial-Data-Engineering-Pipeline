import yfinance as yf
import pandas as pd

stocks = ['META', 'AAPL', 'AMZN', 'NFLX','SAP', 'GOOG', 'NVDA']

def collect_raw_stock_data(stocks, period):
     return yf.download(stocks, period=period, group_by='ticker')

raw_stocks = collect_raw_stock_data(stocks, '6mo')

df = pd.DataFrame(raw_stocks)

df.to_csv('raw_stocks.csv')
