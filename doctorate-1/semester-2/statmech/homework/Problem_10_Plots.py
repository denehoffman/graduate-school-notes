import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
plt.rc('text', usetex=True)


def P(x, mu, sigma_sr):
    return (1 / x * np.sqrt(2 * np.pi * sigma_sr)) \
        * np.exp(-np.power(np.log(x) - mu, 2) / 2 * sigma_sr)


def Mean(sigma_sr):
    return np.exp((1 / 2) * sigma_sr)


x = np.linspace(0, 5, 100000)
sigma_sr_list = [1 / 3, 1, 3]
color_list = ['b', 'g', 'm']
label_list = [r'$\sigma^2 = \frac{1}{3}$', r'$\sigma^2 = 1$', r'$\sigma^2 = 3$']
for i, sigma_sr in enumerate(sigma_sr_list):
    ax.plot(x, P(x, 0, sigma_sr), label=label_list[i], color=color_list[i])
    ax.axvline(Mean(sigma_sr), ls=':', color=color_list[i])
    ax.text(Mean(sigma_sr) + 0.05, 5, 'Mean', rotation=45, color=color_list[i])

ax.axvline(1, ls=':', color='k')
ax.text(0.7, 5.5, 'Median', rotation=45)

ax.legend(loc='best', frameon=False)
ax.set_title(r'Plots of $P_{0,\sigma^2}(x)$ for various values of $\sigma^2$')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$P_{0,\sigma^2}(x)$')
plt.show()
