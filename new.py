#print("hello")
import matplotlib.pyplot as plt
import numpy as np

#height = np.array([167,170])
#weight = np.array([86,74])
#height = np.arange(140, 180, dtype=int)
"""
weight = np.arange(60, 100, dtype=int)
height = np.repeat(141, 40)
height1 = np.repeat(151, 40)
"""
#weight = np.arange(60, 100, dtype=int)


plt.xlim(14,200)
plt.ylim(60,100)
for i in range(141, 200):
    weight = np.arange(60, 100, dtype=int)
    height = np.repeat(i, 40)
    plt.scatter(height, weight)
#plt.scatter(height1, weight)
plt.title("Bubbles")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()