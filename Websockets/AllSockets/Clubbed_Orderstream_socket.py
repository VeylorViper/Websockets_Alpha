from FileSave import *
import matplotlib.pyplot as plt
import time

Activity = LoadH5("Analyze/TestData4.h5","1")

for i in range(30,len(Activity)):
    M1 = sum(Activity[i-1:i])
    M4 = sum(Activity[i-4:i])
    M10 = sum(Activity[i-10:i])
    M15 = sum(Activity[i-15:i])
    M30 = sum(Activity[i-30:i])
    print(int(M1),"\t",int(M4),"\t",int(M10),"\t",int(M15),"\t",int(M30),f"\t Indexing at {i}")
    time.sleep(1)