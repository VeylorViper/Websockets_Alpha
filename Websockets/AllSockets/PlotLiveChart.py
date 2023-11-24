import matplotlib.pyplot as plt
from FileSave import *

Activity = LoadH5("Analyze/TestData4.h5","1")

M1 = []
M4 = []
M10 = []
M15 = []
M30 = []

for i in range(30,len(Activity)):
    M1.append(sum(Activity[i-1:i]))
    M4.append(sum(Activity[i-4:i]))
    M10.append(sum(Activity[i-10:i]))
    M15.append(sum(Activity[i-15:i]))
    M30.append(sum(Activity[i-30:i]))

Neutral = []
for i in range(0,50):
    Neutral.append(0)

for element in Activity[49:65]:
    Neutral.append(element)

plt.plot(Activity[:50],color='black')
plt.plot(Neutral,color='red')
# # plt.plot(M1[:50],color='red')
# # plt.plot(M4[:50],color='blue')
# # plt.plot(M10[:50],color='orange')
# # plt.plot(M15[:50],color='green')
# plt.plot(M30[:50],color='pink')
plt.plot([(i*0) for i, _ in enumerate(Activity[:65])])
plt.savefig("OverActivity.png")