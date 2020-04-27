import numpy as np
from scipy.stats import binom, poisson
import matplotlib.pyplot as plt
'''
fig, ax = plt.subplots(1, 1)

n_list = np.array([50, 60, 70, 100, 200, 400])
p_list = 10 / n_list
x = np.arange(poisson.ppf(0.01, 10), poisson.ppf(0.99, 10))
for i in range(len(n_list)):
    ax.plot(x, binom.pmf(x, n_list[i], p_list[i]), ms=8, label='Binomial: N = {}'.format(n_list[i]))
ax.plot(x, poisson.pmf(x, 10), ms=8, label='Poisson')
ax.legend(loc='best', frameon=False)
plt.show()
'''

print(poisson.cdf(132, 100))
