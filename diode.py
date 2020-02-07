import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.65, 0.68, 0.7, 0.75])
y = np.array([0, 0, 0, 0, 0, 0, 0.01, 0.8, 1.2, 1.9, 3.0, 2.5, 4.5, 7.2, 18.1])
yerror = [0.1] * 15

#plt.plot(x,y,'x')
plt.errorbar(x, y, yerr=yerror, fmt='.', color='k', capsize=2, ecolor='k')
plt.title("Graph showing the potential difference across a diode against current")
plt.xlabel("p.d./V")
plt.ylabel("I/A")
plt.savefig("forChar.jpg", dpi=300)