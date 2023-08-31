# %%
pip install ccxt

# %%
import time
import ccxt

# %%
exchange = ccxt.binance({})

# %%
#Consutla de Ticker BTC
exchange.fetchTicker('BTC/USDT')

# %%
#Consulta de Ticker, solo parametro 'last' para saber el ultimo precio
exchange.fetchTicker('BTC/USDT')['last']