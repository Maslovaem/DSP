import matplotlib.pyplot as plt
import math
import numpy as np

def transform_polynom(b, a, beta, alpha, x, y):
    N = len(b)- 1
    P = len(beta)-1
    B_matrix = np.zeros((N+1, N*P+1))
    A_matrix = np.zeros((N+1, N*P+1))
    B_matrix[N, N*P] = 1.0
    A_matrix[N, N*P] = 1.0
    for i in range(N):
        v = np.convolve(B_matrix[-i-1, :], beta)
        B_matrix[-i-2] = v[len(v)-N*P-1::]
        v = np.convolve(A_matrix[-i-1, :], alpha)
        A_matrix[-i-2] = v[len(v)-N*P-1::]
    for i in range(N+1):
        v = np.convolve(B_matrix[i, :], A_matrix[-i-1, :])
        x += v[len(v)- N*P-1::] * a[i]
        y += v[len(v)- N*P-1::] * b[i]

#Дано:
F_s = 5*1000000;

f_pl = 1*1000000;
f_ph = 2*1000000;
f_sl = 1.2*1000000;
f_sh = 1.8*1000000;

R_p = 2;
R_s = 60;

#Нормировка к частоте дискретизации:
f_pl = f_pl*2*math.pi/F_s;
f_ph = f_ph*2*math.pi/F_s;
f_sl = f_sl*2*math.pi/F_s;
f_sh = f_sh*2*math.pi/F_s;

print("f_pl = ", f_pl);
print("f_ph = ", f_ph);
print("f_sl = ", f_sl);
print("f_sh = ", f_sh);

#Частоты аналогового фильтра, соответствующие частотам цифрового фильтра, нормированного к частоте дискретризации:
omega_pl = 2*math.tan(f_pl/2);
omega_ph = 2*math.tan(f_ph/2);
omega_sl = 2*math.tan(f_sl/2);
omega_sh = 2*math.tan(f_sh/2);

print("omega_pl = ", omega_pl);
print("omega_ph = ", omega_ph);
print("omega_sl = ", omega_sl);
print("omega_sh = ", omega_sh);

#Расчёт параметров аналогового фильтра
omega_c = math.sqrt(omega_sl*omega_sh);
B = omega_sh - omega_sl;

print("omega_c = ", omega_c);
print("B = ", B);

#Определяем, по какой полосе рассчитывать omega_s;
ksi_ph = (omega_c**2)/omega_ph;

print("ksi_ph = ", ksi_ph);

#ksi_ph < omega_pl => рассчитываем по нижней переходной полосе
omega_s = (-1)*omega_sl*B/(omega_sl**2 - omega_c**2);
omega_p = (-1)*omega_pl*B/(omega_pl**2 - omega_c**2);

print("omega_s = ", omega_s);
print("omega_p = ", omega_p);

#omega_s = 1, т.к. нам нужен фильтр Чебышева 2 рода, то преобразование ФНЧ-ФНЧ не делаем
#Расчёт передаточной характеристики нормированного ФНЧ Чебышева 2 рода
eps_p = math.sqrt(10**(R_p/10) - 1);
eps_s = math.sqrt(10**(R_s/10) - 1);

print("eps_s = ", eps_s);
print("eps_p = ", eps_p);

#Расчёт порядка фильтра
N = (np.arccosh(eps_s/eps_p)) / (np.arccosh(omega_s/omega_p));
print("N = ", N); #Берём N = 7
N = 7

#Расчёт beta
beta = (1/N)*np.arccosh(eps_s)
print("beta = ", beta)

#Расчёт alpha_i
alpha = [0]*(N//2)

for i in range (N//2):
    alpha[i] = (2*(i + 1) - 1)*math.pi / (2*N)

for i in range (N//2):
    print("alpha_", i+1,"=", alpha[i])

#Расчёт sigma_i
sigma = [0]*(N//2)

for i in range (N//2):
    sigma[i] = (-1)*math.sin(alpha[i])*np.sinh(beta) / ((math.cos(alpha[i])*np.cosh(beta))**2 + (math.sin(alpha[i])*np.sinh(beta))**2)

for i in range (N//2):
    print("sigma_", i + 1, "=", sigma[i])    

#Расчёт omega_i:
omega = [0]*(N//2)

for i in range (N//2):
    omega[i] = math.cos(alpha[i])*np.cosh(beta) / ((math.cos(alpha[i])*np.cosh(beta))**2 + (math.sin(alpha[i])*np.sinh(beta))**2)

for i in range (N//2):
    print("omega_", i + 1, "=", omega[i]) 

#Расчёт sigma_i**2 + omega_i**2
x = [0]*(N//2)

for i in range (N//2):
    x[i] = sigma[i]**2 + omega[i]**2

for i in range (N//2):
    print("omega_", i + 1, "**2 + sigma_", i + 1, "**2 =", x[i])

#Расчёт G_0
G_0 = 1;
sigma_0 = (-1)/np.sinh(beta);
print("sigma_0 =", sigma_0);

y = [0]*(N//2) #1/cos(alpha_i)**2
for i in range (N//2):
    y[i] = 1/(math.cos(alpha[i]))**2

for i in range (N//2):
    G_0 *= (y[i] / x[i])

G_0 /= (-1)*sigma_0
print("G_0 =", G_0)

#Считаем Hn(s):
n = np.array([1])
for i in range(N//2):
    n = np.convolve(n, [1, 0, y[i]])
n /= G_0

d = np.array([1])
for i in range(N//2):
    d = np.convolve(d, [1, -2*sigma[i], x[i]])

d = np.convolve(d, [1, -sigma_0])

print("Norm fnch cheb2 num:", n)
print("Norm fnch cheb2 denom:", d)

#так как фильтр режекторный, то преобразование ФНЧ-ФНЧ не делаем
#преобразование ФНЧ-РФ
n = np.pad(n, (N + 1 - len(n), 0), mode = 'constant')
d = np.pad(d, (N + 1 - len(d), 0), mode = 'constant')
beta_string = np.array([0.0, B, 0.0])
alpha_string = np.array([1.0, 0.0, omega_c**2])
P = len(beta_string) - 1
n_res = np.zeros(N*P+1)
d_res = np.zeros(N*P+1)

transform_polynom(n, d, beta_string, alpha_string, d_res, n_res)
print("fnch-rf num =", n_res)
print("fnch-rf denom =", d_res)

#Билинейное преобразование:
n_res_digital = np.zeros(N*P+1)
d_res_digital = np.zeros(N*P+1)
transform_polynom(n_res, d_res, [2.0, -2.0], [1.0, 1.0], d_res_digital, n_res_digital)
print("digital num =", n_res_digital / d_res_digital[-1])
print("digitital denom =", d_res_digital / d_res_digital[-1])