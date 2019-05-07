import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2, 1000)

y = 1/2

sines = [2/(np.pi*n) * np.sin(n*2*np.pi*t) for n in range(1, 50, 2)]

for sine in sines:
    y = y + sine

plt.figure()
plt.title('Fourier series of square wave')
for sine in sines:
    plt.plot(t, sine)
plt.plot(t, y, 'black')
plt.show()
