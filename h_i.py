import numpy as np
import matplotlib.pyplot as plt

b = [0.04832, -0.01893, 0.04458, 0.04458, -0.01893, 0.04832] 
a = [1, -2.43900, 2.79000, -1.67300, 0.53850, -0.06838]
N = 40
h = [0]*N
x = [0]*N
x[0] = 1

for n in range(N):
    h[n] = sum(b[k]*x[n - k] for k in range(6)) - sum(a[k]*h[n - k] for k in range(6))

plt.axis([0, 40, -0.1, 0.25])
markerline, stemline, baseline, = plt.stem(np.arange(N), h, linefmt='-',markerfmt='o',basefmt=' ')
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 2)
plt.title('Импульсная характеристика')
plt.xlabel('k')
plt.ylabel(r'$h_{\text{и}}$')
plt.grid(visible=True, which='major', color='gray', linestyle='--', linewidth=0.5)
plt.show()