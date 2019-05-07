import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 4, 1000)

y = 1/2

cosines = [-4/(np.pi*np.pi*n*n) * np.cos(n*np.pi*t) for n in range(1, 20, 2)]

for cosine in cosines:
    y = y + cosine

plt.figure()
plt.title('Fourier series of triangle wave')
for cosine in cosines:
    plt.plot(t, cosine)
plt.plot(t, y, 'black')
plt.show()
