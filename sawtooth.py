import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2, 1000)

y = 1/2

sines = [-1/(2*n*np.pi) * np.sin(2*np.pi*n*t) for n in range(1, 50, 1)]

for sine in sines:
    y = y + sine

plt.figure()
plt.title('Fourier series of sawtooth wave')
for sine in sines:
    plt.plot(t, sine)
plt.plot(t, y, 'black')
plt.show()
