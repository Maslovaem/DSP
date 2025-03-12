import matplotlib.pyplot as plt
import math
import cmath
import numpy as np

plt.axis([0, math.pi*2, math.pi*(-5/4), math.pi*(5/4)])
plt.title('ФЧХ')
plt.gca().set_ylabel(r'$\Phi (\omega)$, рад')
plt.gca().set_xlabel(r'$\omega$')
plt.xticks([0, math.pi*0.5, math.pi, math.pi*1.5, math.pi*2], [r'0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
plt.yticks([math.pi*(-1), math.pi*(-0.5), 0, math.pi*0.5, math.pi], [r'$-\pi$', r'$\frac{-\pi}{2}$', r'0', r'$\frac{\pi}{2}$', r'$\pi$'])
plt.grid(visible=True, which='major', color='gray', linestyle='--', linewidth=0.5)

N = 100
x = np.linspace(0, math.pi*2, N)

z = [0]*N
y = [0]*N

for i in range(N):
    z[i] = np.exp(1j * x[i])

for i in range(N):
    B = (0.04832 - 0.01893 * z[i]**-1 + 0.04458 * z[i]**-2 + 0.04458 * z[i]**-3 - 0.01893 * z[i]**-4 + 0.04832 * z[i]**-5)
    A = (1 - 2.43900 * z[i]**-1 + 2.79000 * z[i]**-2 - 1.67300 * z[i]**-3 + 0.53850 * z[i]**-4 - 0.06838 * z[i]**-5)
    H = B/A
    y[i] = cmath.phase(H)

plt.plot(x, y)
plt.show()