import pyupbit
from dotenv import load_dotenv 
import os

load_dotenv()
access = os.environ["access"]  #access 키
secret = os.environ["secret"]  #secret 키
upbit = pyupbit.Upbit(access, secret)

tickers = pyupbit.get_tickers("KRW")
tickers 

df=pyupbit.get_ohlcv("KRW-BTC","minute5")
df 

try:
  upbit = pyupbit.Upbit(access, secret)
  print("Login COMPLETE")
  print("====================================")
except:
  print("!!Login ERROR!!")


def get_balance_cash():
    return upbit.get_balance("KRW")


