from coin_proto.where_now import tickers

def test_tickers():
    t = print(tickers)
    assert t == 'KRW-BTC'
