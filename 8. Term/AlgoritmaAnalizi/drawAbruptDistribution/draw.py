# poisson + binomial + bernoulli + geometric + hypergeometric

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def poisson():
    rate = 2
    n = np.arange(0, 10)
    y = stats.poisson.pmf(n, rate)
    print(y)
    plt.plot(n, y, 'o-')
    plt.title('Poisson: $\lambda$ ={}' .format(rate))
    plt.xlabel('Kaza sayısı')
    plt.ylabel('Gerçekleşme olasılığı')
    plt.show()


def binomial():
    n = 10
    p = 0.3
    k = np.arange(0, 21)
    binom = stats.binom.pmf(k, n, p)
    print(binom)
    plt.plot(k, binom, 'o-')
    plt.title('Binomail: n={} , p={}' .format(n, p))
    plt.xlabel('Başarı sayısı')
    plt.ylabel('Başarı ihtimali')
    plt.show()


def bernoulli():
    p = 0.3
    k = np.arange(0, 21)
    bernoul = stats.bernoulli.pmf(k, p)
    print(bernoul)
    plt.plot(k, bernoul, 'o-')
    plt.title('Bernoulli:  p={}' .format(p))
    plt.xlabel('Başarı sayısı')
    plt.ylabel('Başarı ihtimali')
    plt.show()


def geometric():
    p = 0.5
    k = np.arange(0, 21)
    geom = stats.geom.pmf(k, p)
    print(geom)
    plt.plot(k, geom, 'o-')
    plt.title('Geometric:  p={}' .format(p))
    plt.xlabel('Başarı sayısı')
    plt.ylabel('Başarı ihtimali')
    plt.show()


def hypergeometric():
    [M, n, N] = [20, 7, 12]
    k = np.arange(0, n + 1)
    hypergeom = stats.hypergeom.pmf(k, M, n, N)
    print(hypergeom)
    plt.plot(k, hypergeom, 'o-')
    plt.title('Hyper Geometric:  M:{} n: {} N: {}' .format(M, n, N))
    plt.xlabel('Başarı sayısı')
    plt.ylabel('Başarı ihtimali')
    plt.show()

poisson()
bernoulli()
binomial()
geometric()
hypergeometric()