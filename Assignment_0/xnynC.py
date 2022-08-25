import pandas as pd
import numpy as np

x = pd.read_csv('x.txt',header=None)
print(x)

y = pd.read_csv('y.txt',header=None)
print(y)

import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output in C')
plt.ylabel('$x(n)$')
plt.grid()


plt.subplot(2, 1, 2)
plt.stem(range(0,20),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('xnynC.pdf')
