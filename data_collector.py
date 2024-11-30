import yfinance as yf
import pandas as pd
from access_vault import service_client

stocks = ['META', 'AAPL', 'AMZN', 'NFLX','SAP', 'GOOG', 'NVDA']

def collect_raw_stock_data(stocks, period):
     return yf.download(stocks, period=period, group_by='ticker')

raw_stocks = collect_raw_stock_data(stocks, '6mo')

df = pd.DataFrame(raw_stocks)

df.to_csv('raw_stocks.csv')

def upload_file(container_name:str, local_file_path:str, destination_path:str):
     file_system_client = service_client.get_file_system_client(file_system=container_name)
     file_client = file_system_client.get_file_client(destination_path)

     with open(local_file_path, 'rb') as file:
          file_client.upload_data(file, overwrite=True)
