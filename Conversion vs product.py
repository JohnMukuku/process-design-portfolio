import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,1, 50)
A_in = 100

B_out = A_in * X

plt.plot(X, B_out)
plt.xlabel("Conversion")
plt.ylabel("B Production (kmol/h)")
plt.title("Effect of Conversion on Product Formation")
plt.show()