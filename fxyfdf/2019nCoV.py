
# https://blog.csdn.net/jiazhen/article/details/104097135/

import numpy as np
import matplotlib.pyplot as plt

gamma = 0.55
Q = 7
D = 10
P = np.zeros(300, dtype=np.float)
Psum = np.zeros(300, dtype=np.float)
for i in range(Q):
    P[i] = 1
for j in range(300 - Q):
    P[j + Q] = P[j + Q - 1] + P[j] * gamma
    if j + Q - D - Q >= 0:
        P[j + Q] -= P[j + Q - D - Q] * gamma
    if j + Q == D:
        P[j + Q] -= 1
plt.xlabel("N")
plt.ylabel("PN")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(range(1, 61), P[0:60])

plt.grid()
plt.show()
