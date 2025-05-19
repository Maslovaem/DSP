import numpy as np
import matplotlib.pyplot as plt

N = 39

h = [-1.39590886e-19, -6.00083153e-05,  2.41695545e-04, -2.03043229e-04,
 -5.74360390e-04,  2.03781367e-03, -2.93308428e-03,  1.23004088e-03,
  4.01428612e-03, -1.04434786e-02,  1.21682714e-02, -3.23428337e-03,
 -1.63316540e-02,  3.62231938e-02, -3.81069617e-02,  5.43527628e-03,
  6.41922792e-02, -1.52694759e-01,  2.27250986e-01,  7.43589744e-01,
  2.27250986e-01, -1.52694759e-01,  6.41922792e-02,  5.43527628e-03,
 -3.81069617e-02,  3.62231938e-02, -1.63316540e-02, -3.23428337e-03,
  1.21682714e-02, -1.04434786e-02,  4.01428612e-03,  1.23004088e-03,
 -2.93308428e-03,  2.03781367e-03, -5.74360390e-04, -2.03043229e-04,
  2.41695545e-04, -6.00083153e-05, -1.39590886e-19]

plt.axis([0, 40, -0.2, 0.8])
markerline, stemline, baseline, = plt.stem(np.arange(N), h, linefmt='-',markerfmt='o',basefmt=' ')
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 2)
plt.title('Импульсная характеристика')
plt.xlabel('k')
plt.ylabel(r'$h_{\text{и}}$')
plt.grid(visible=True, which='major', color='gray', linestyle='--', linewidth=0.5)
plt.show()