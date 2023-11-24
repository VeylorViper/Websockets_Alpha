from pybit.unified_trading import WebSocket
import time,h5py 

def SaveH5(filename, data_array,dataset):
    try:
        with h5py.File(filename, 'a') as file:
            dataset = file.create_dataset(f"{dataset}",data=data_array)
    except Exception as e:
        print(f"Error: {e}")
        
messages = []      
try:
    ws = WebSocket(
        testnet=False,
        channel_type='linear'
    )

    
    def handleMessage(message):
        try:
            messages.append(message['data']['bid1Price'])
            print(message['data']['bid1Price'])
        except Exception as f:
            print("Error occured in the function `handle message` : ",f)
        
    ws.ticker_stream(
        symbol='ETHUSDT',
        callback=handleMessage
    )

    print("Starting")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    SaveH5("Prices.h5",messages,"1")
