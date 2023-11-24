from pybit.unified_trading import WebSocket 
import time 
from FileSave import *

Prices = []
TimeStamps = []

try:
    ws = WebSocket(
        testnet=False,
        channel_type='linear'
    )

    def handle_message(message):
        Prices.append(message['data']['bid1Price'])
        TimeStamps.append(message['ts'])
        print("Confirm")
        
    ws.ticker_stream(
        symbol='ETHUSDT',
        callback=handle_message
    )
    
    print("Starting Prices")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    SaveH5("RD_Prices.h5",Prices,"1")
    SaveH5("TimestampsPrices.h5",TimeStamps,'1')