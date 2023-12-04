import pandas as pd
import matplotlib.pyplot as plt
with open("data_test1.txt") as f:
    data=f.read()
data=data.split('\n')
x=[row.split(' ')[0] for row in data]
y=[row.split(' ')[1] for row in data]
z=[row.split(' ')[2] for row in data]

plt.plot(x,y,z)
plt.show()