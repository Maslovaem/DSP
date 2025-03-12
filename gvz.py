import matplotlib.pyplot as plt
import math
import cmath
import numpy as np

plt.axis([0, math.pi/2, 0, 12])
plt.title('ГВЗ')
plt.gca().set_ylabel(r'$\tau_g (\omega)$')
plt.gca().set_xlabel(r'$\omega$')
plt.xticks([0, math.pi/8, math.pi/4, math.pi*(3/8), math.pi/2], [r'0', r'$\frac{\pi}{8}$', r'$\frac{\pi}{4}$', r'$\frac{3\pi}{8}$', r'$\frac{\pi}{2}$'])
plt.yticks([0, 2, 4, 6, 8, 10, 12], [0, 2, 4, 6, 8, 10, 12])
plt.grid(visible=True, which='major', color='gray', linestyle='--', linewidth=0.5)

N = 1000
x = np.linspace(0, math.pi/2, N)

y = [0]*N
A = [0]*N
B = [0]*N
C = [0]*N
D = [0]*N

dA = [0]*N
dB = [0]*N
dC = [0]*N
dD = [0]*N

F = [0]*N
E = [0]*N

for i in range(N):
    A[i] = 0.04832 - 0.01893*math.cos(x[i]*1) + 0.04458*math.cos(x[i]*2) + 0.04458*math.cos(x[i]*3) - 0.01893*math.cos(x[i]*4) + 0.04832*math.cos(x[i]*5)
    B[i] = (-1)*(- 0.01893*math.sin(x[i]*1) + 0.04458*math.sin(x[i]*2) + 0.04458*math.sin(x[i]*3) - 0.01893*math.sin(x[i]*4) + 0.04832*math.sin(x[i]*5))
    C[i] = 1 - 2.43900*math.cos(x[i]*1) + 2.79000*math.cos(x[i]*2) - 1.67300*math.cos(x[i]*3) + 0.53850*math.cos(x[i]*4) - 0.06838*math.cos(x[i]*5)
    D[i] = (-1)*( - 2.43900*math.sin(x[i]*1) + 2.79000*math.sin(x[i]*2) - 1.67300*math.sin(x[i]*3) + 0.53850*math.sin(x[i]*4) - 0.06838*math.sin(x[i]*5))

for i in range(N):
    dA[i] = (-1)*(- 0.01893*math.sin(x[i]*1)*1 + 0.04458*math.sin(x[i]*2)*2 + 0.04458*math.sin(x[i]*3)*3 - 0.01893*math.sin(x[i]*4)*4 + 0.04832*math.sin(x[i]*5)*5)
    dB[i] = (-1)*(- 0.01893*math.cos(x[i]*1)*1 + 0.04458*math.cos(x[i]*2)*2 + 0.04458*math.cos(x[i]*3)*3 - 0.01893*math.cos(x[i]*4)*4 + 0.04832*math.cos(x[i]*5)*5)
    dC[i] = (-1)*(- 2.43900*math.sin(x[i]*1)*1 + 2.79000*math.sin(x[i]*2)*2 - 1.67300*math.sin(x[i]*3)*3 + 0.53850*math.sin(x[i]*4)*4 - 0.06838*math.sin(x[i]*5)*5)
    dD[i] = (-1)*( - 2.43900*math.cos(x[i]*1)*1 + 2.79000*math.cos(x[i]*2)*2 - 1.67300*math.cos(x[i]*3)*3 + 0.53850*math.cos(x[i]*4)*4 - 0.06838*math.cos(x[i]*5)*5)

for i in range(N):
    F[i] = dA[i]*C[i] + A[i]*dC[i] + dB[i]*D[i] + B[i]*dD[i]
    E[i] = dB[i]*C[i] + B[i]*dC[i] - dA[i]*D[i] - A[i]*dD[i]

for i in range(N):
    y[i] = (F[i]*(B[i]*C[i] - A[i]*D[i]) - E[i]*(A[i]*C[i] + B[i]*D[i]))/((A[i]**2 + B[i]**2)*(C[i]**2 + D[i]**2))

plt.plot(x, y)
plt.show()