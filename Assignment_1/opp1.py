import numpy as np
from scipy import signal, vectorize
from matplotlib import pyplot as plt

N = 100
num = [1, 0, -0.5]
den = [1, -0.75, 0.125]
r, p, k = signal.residuez(num, den)
rp_args = np.arange(N)

def rp(x):
    return r@(p**x).T

rp_vec = vectorize(rp, otypes=['double'])
h1 = rp_vec(rp_args)
k_add = np.pad(k, (0, N - len(k)), 'constant', constant_values=(0,0))
h = h1 + k_add
plt.stem(rp_args, h)
plt.xlabel('n')
plt.ylabel('$h(n)$')
plt.grid()
plt.show()
plt.savefig('op1.pdf')