from pybit.unified_trading import WebSocket 
import time 
from PostData import *

def _create_connection():
    ws = WebSocket(
        testnet=False,
        channel_type='linear')
    return ws

orders = []
def OrderBookStream():
    global orders
    try:
        ws = _create_connection()
        
        def _stream_data(ws):
            def handleMessage(message):
                postdata(float(message['data']['b'][0][1]) - float(message['data']['a'][0][1]))
                
            ws.orderbook_stream(
                depth=1,
                symbol='ETHUSDT',
                callback = handleMessage
            )
            
            print("Starting")
            while True:
                time.sleep(0.1)
            
        _stream_data(ws)
    except Exception as e:
        print("Error occured : ",e)
        OrderBookStream()
    
    
if __name__ == '__main__':
    OrderBookStream()