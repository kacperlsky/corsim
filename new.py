#print("hello")
import matplotlib.pyplot as plt
import numpy as np

height = np.array([167,170])
weight = np.array([86,74])

plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height, weight)
plt.title("Bubbles")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()