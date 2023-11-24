from pybit.unified_trading import WebSocket 
import time 
from FileSave import *

Orders = []
TimeStamps = []

try:
    ws = WebSocket(
        testnet=False,
        channel_type='linear'
    )

    def handle_message(message):
        Orders.append(float(message['data']['b'][0][1]) - float(message['data']['a'][0][1]))
        TimeStamps.append(message['ts'])
        print("Confirm")
        
    ws.orderbook_stream(
        depth=1,
        symbol='ETHUSDT',
        callback=handle_message
    )
    
    print("Starting")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    SaveH5("RD_Orders.h5",Orders,"1")
    SaveH5("TimestampsOrders.h5",TimeStamps,'1')