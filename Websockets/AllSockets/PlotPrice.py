import matplotlib.pyplot as plt 
from FileSave import *

Prices = LoadH5("Prices.h5",'1')
_Prices = []
for element in Prices:
    _Prices.append(float(element))
    
plt.plot(_Prices)
plt.show()