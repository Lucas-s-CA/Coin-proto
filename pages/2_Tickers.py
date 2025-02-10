import pyupbit
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import psycopg

url = "https://api.upbit.com/v1/market/all"
res = requests.get(url).json()

ticker_list = {}

for i in res:
    name = i['korean_name']
    ticker = i['market']

    if ticker.startswith("KRW"):
        ticker_list[name] = ticker

ticker_list

