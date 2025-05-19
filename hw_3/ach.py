#-*- coding: utf-8-*
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

def fir_lpf(N, bp):
# Задаем АЧХ
 H = np.zeros(N+1)
 H[0
 : bp+1] = 1.0
 H[N- bp+1 : N+1 ] = 1.0
 # Задаем ФЧХ
 PHI = H*0
 if N%2:
    k = np.arange(0, int((N-1)/2)+1)
    PHI[k] =-k * N * np.pi / (N+1)
    k = np.arange(int((N-1)/2)+1, N+1)
    PHI[k] = N * np.pi-k * N * np.pi / (N+1)
 else:
    k = np.arange(0, int(N/2)+1)
    PHI[k] =-k * N * np.pi / (N+1)
    k = np.arange(int(N/2)+1, N+1)
    PHI[k] = N * np.pi- k * N * np.pi / (N+1)
 # ОБПФ частотной выборки
 return np.fft.ifft(H*np.exp(1j*PHI))

Fs = 30000
fp = 10000
fs = 13000
Rp = 1
Rs = 60

#Выбираем окно Блэкмана, т.к оно обеспечивает нужно затухание в полосе задержания
BW0 = 8.26
#Оценка порядка фильтра
N = int( BW0/2 * Fs*Rs/ (fs- fp)/22)+1
print(N)
#После визуализации АЧХ видим, что порядок фильтра может быть уменьшен
N = 38
#Бин ДПФ, соответствующий fp
bp = int(fp * (N+1) / Fs)+1
print("bp = ", bp)
h = fir_lpf(N, bp)
#Чтобы избежать растекания спектра, домножаем на оконную функцию
h = h * signal.windows.blackman(N + 1)
w = np.linspace(0, np.pi, 1024)
f, Hw = signal.freqz(h, 1, w)
plt.plot(w/np.pi, 20*np.log10(np.abs(Hw)))
plt.grid(True)
plt.ylim([-150, 10])

plt.axhline(y = -Rs, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axhline(y = -Rp, color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = fs/(Fs/2), color = '#ff7f0e', linestyle = '-', lw = 1)
plt.axvline(x = fp/(Fs/2), color = '#ff7f0e', linestyle = '-', lw = 1)

plt.show()
