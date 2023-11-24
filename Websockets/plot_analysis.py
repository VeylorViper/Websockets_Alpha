import matplotlib.pyplot as plt 
from FileSave import *

Orders = LoadH5("Analyze/RD_Orders.h5",'1')
_Prices = LoadH5("Analyze/RD_Prices.h5",'1')
OrderTS = LoadH5("Analyze/TimestampsOrders.h5",'1')
PricesTS = LoadH5("Analyze/TimestampsPrices.h5",'1')
Neutral = [(i*0) for i, _ in enumerate(Orders)]
Prices = []
for price in _Prices:
    Prices.append(float(price))

plt.subplot(2,1,1)
plt.plot(PricesTS,Prices)
plt.title('Prices')

plt.subplot(2,1,2)
plt.plot(OrderTS[1:],Orders)
plt.plot(OrderTS[6:],SalesOverview(Orders,5),color='red')
plt.plot(OrderTS[1:],Neutral,color='orange')
plt.title('Orders')

plt.tight_layout()
plt.show()