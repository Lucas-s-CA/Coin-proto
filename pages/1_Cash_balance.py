import pyupbit
import streamlit as st
from dotenv import load_dotenv
import json
import os
import pandas as pd
import psycopg

load_dotenv()
access = os.getenv("access")  #access 키
secret = os.getenv("secret")  #secret 키
upbit = pyupbit.Upbit(access, secret)


def get_balance(ticker):
    balances = upbit.get_balances()

    # API 응답이 문자열이면 JSON으로 변환
    if isinstance(balances, str):
        balances = json.loads(balances)

    # balances가 리스트인지 확인 후 처리
    if isinstance(balances, list):
        for b in balances:
            if b['currency'] == ticker:
                return float(b['balance']) if b['balance'] is not None else 0
    return 0  # 잔액이 없을 경우 0 반환

ticker = 'KRW'
balance = get_balance(ticker)
st.write(f"{ticker} 잔액: {balance}")
