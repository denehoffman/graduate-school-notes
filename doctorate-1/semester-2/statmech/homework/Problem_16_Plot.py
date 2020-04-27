import numpy as np
import matplotlib.pyplot as plt


def P(h, mu):
    return 4 * h / np.power(mu, 2) * np.exp(-2 * h / mu)


h_range = np.linspace(0, 10, 500)
mu_list = [1, 2, 3, 4]
for mu in mu_list:
    plt.plot(h_range/mu, P(h_range, mu), label=r"$\mu =$ {}".format(mu))
plt.axvline(1, ls=":", color='k')
plt.legend()
plt.title(r"$P_{\mu}(h)$ vs $\frac{h}{\mu}$")
plt.xlabel(r"$\frac{h}{\mu}$")
plt.ylabel(r"$P_{\mu}(h)$ ($m^{-1}$)")
plt.show()
