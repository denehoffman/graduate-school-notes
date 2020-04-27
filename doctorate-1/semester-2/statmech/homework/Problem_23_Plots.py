import numpy as np
import matplotlib.pyplot as plt


def f(x, a):
    return np.power(x, 4) / 4 - a * np.power(x, 2) / 2


def p(x, a):
    return np.power(x, 3) - a * x


def alph(p, a):
    return np.arccos(3 * np.sqrt(3) * p / 2 / np.power(a, 3 / 2)) / 3


def x(a, alpha, k):
    return np.sqrt(4 * a / 3) * np.cos(alpha + 2 * np.pi / 3 * k)

pa = np.linspace(-5, 5, 200)
x0 = x(1, alph(pa, 1), 0)
x1 = x(1, alph(pa, 1), 1)
x2 = x(1, alph(pa, 1), 2)
plt.plot(p(x0, 1), f(x0, 1) - p(x0, 1) * x0, label=r"$x_0$")
plt.plot(p(x1, 1), f(x1, 1) - p(x1, 1) * x1, label=r"$x_1$")
plt.plot(p(x2, 1), f(x2, 1) - p(x2, 1) * x2, label=r"$x_2$")

plt.axhline(0, color='k', ls='--')
plt.axvline(0, color='k', ls='--')
plt.legend()

plt.show()
