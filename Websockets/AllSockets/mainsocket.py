from pybit.unified_trading import WebSocket
from time import sleep,time
import h5py

def SaveH5(filename, data_array,dataset):
    try:
        with h5py.File(filename, 'a') as file:
            dataset = file.create_dataset(f"{dataset}",data=data_array)
    except Exception as e:
        print(f"Error: {e}")

try:
    ws = WebSocket(
        testnet=False,
        channel_type="linear",
    )

    D = 0
    message = []
    def handle_message(message1):
        print(message1['ts'])
        # try:
        #     global D,message
        #     if D == 40:
        #         message.append(float(message1['data']['b'][0][1]) - float(message1['data']['a'][0][1]))
        #         print("Appended")
        #         D = 0
        #     else : 
        #         D += 1
        # except Exception as e:
        #     D += 1
        #     print(e)

    ws.orderbook_stream(
        depth=1,
        symbol='ETHUSDT',
        callback= handle_message
    )

    print("Starting")
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    SaveH5("TestData4.h5",message,"1")