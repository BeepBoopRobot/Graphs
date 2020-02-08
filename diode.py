import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.85,2.50,2.13,1.79,1.65])
y = np.array([7.50,6.38,5.71,5.10,4.79])
yerror = []

# plt.plot(x,y,'x')
plt.plot(x, y, '.')
plt.title("Graph showing the potential difference across a diode against current")
plt.xlabel("p.d./V")
plt.ylabel("f/ $Hz \times 10^14$")
plt.show()
#plt.savefig("LED.jpg", dpi=300)
