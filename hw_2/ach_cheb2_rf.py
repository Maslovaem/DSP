import matplotlib.pyplot as plt
import math
import numpy as np

F_s = 5;

f_pl = 1;
f_ph = 2;
f_sl = 1.2;
f_sh = 1.8;

R_p = 2;
R_s = 60;

plt.axvline(x = f_pl, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = f_ph, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = f_sl, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = f_sh, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = f_pl, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axhline(y = -R_s, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axhline(y = -R_p, color = '#ff7f0e', linestyle = '-', lw = 1)


plt.axis([0, 2.5, -80, 5])
plt.gca().set_ylabel(r'$|H(e^{j\omega / F_s})|^{2}$, dB')
plt.gca().set_xlabel('f, кГц')
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6], [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6])
plt.grid(visible = True, which = 'major', color = 'gray', linestyle = '--', linewidth = 0.5)

N = 1000
x = np.linspace(0, F_s, N)

z = [0] * N
y = [0] * N

for i in range(N):
    z[i] = np.exp(1j * x[i] * 2 * math.pi / F_s)

for i in range(N):
    B = (0.11484749 + 0.49685757 * z[i]**-1 + 1.62302904 * z[i]**-2 + 3.61003369 * z[i]**-3 + 6.71890039 * z[i]**-4 + 9.98497658 * z[i]**-5 + 12.84209944 * z[i]**-6 + 13.74342877 * z[i]**-7 + 12.84209944 * z[i]**-8 + 9.98497658 * z[i]**-9 + 6.71890039 * z[i]**-10 + 3.61003369 * z[i]**-11 + 1.62302904 * z[i]**-12 + 0.49685757 * z[i]**-13 + 0.11484749 * z[i]**-14)
    A = (1.31854881e-02 + 7.34699729e-02 * z[i]**-1 + 3.08110334e-01 * z[i]**-2 + 8.88156596e-01 * z[i]**-3 + 2.14618742e+00 * z[i]**-4 + 4.18819350e+00 * z[i]**-5 + 7.10006140e+00 * z[i]**-6 + 1.01578661e+01 * z[i]**-7 + 1.27978176e+01 * z[i]**-8 + 1.36951360e+01 * z[i]**-9 + 1.27793752e+01 * z[i]**-10 + 9.84097391e+00 * z[i]**-11 + 6.45301528e+00 * z[i]**-12 + 3.08336833e+00 * z[i]**-13 + 1.00000000e+00 * z[i]**-14)
    H = B/A
    y[i] = 20 * np.log10(abs(H))

plt.plot(x, y)
plt.show()
