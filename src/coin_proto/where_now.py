import pyupbit 
import typer
import time
from datetime import datetime
from pytz import timezone
import pandas as pd
import json
from dotenv import load_dotenv 
import os

access = ""  # Upbit API access 키
secret = ""  # Upbit API secret 키
try:
  upbit = pyupbit.Upbit(access, secret)
  print("Login COMPLETE")
  
except:
  print("!!Login ERROR!!")


def tickers():
     t = pyupbit.get_tickers("KRW")	# KRW를 통해 거래되는 코인만 불러오기
     print(t)

def df = pyupbit.get_ohlcv("KRW-BTC", "minute5")
    print(df)


def entry_point():
     typer.run(tickers)

