import numpy as np


def riemanKiri(h, f, n):
    result = h * sum(f[:n - 1])
    print("Rieman Kiri : ", result)


def riemanKanan(h, f):
    result = h * sum(f[1::])
    print("Rieman Kanan : ", result)


def riemanTengah(h, x, n):
    result = h * sum(np.cos(2 * np.pi * (x[:n-1] + x[1:]) / 2))
    print("Rieman Tengah : ", result)


def metodeTrapesium(h, f, n):
    result = (h / 2) * (f[0] + 2 * sum(f[1:n-1]) + f[n-1])
    print("Metode Trapesium : ", result)


def metodeSimson(h, f, n):
    result = (h / 3) * (f[0] + 2 * sum(f[:n-2:2]) + 4 * sum(f[1:n-1:2]) + f[n-1])
    print("Metode Simson : ", result)


if __name__ == "__main__":
    a = 0
    b = 1
    n = 4
    h = (b - a) / n
    x = np.linspace(a, b, n)
    fx = np.cos(2 * np.pi * x)
    riemanKiri(h, fx, n)
    riemanKanan(h, fx)
    riemanTengah(h, x, n)
    metodeTrapesium(h, fx, n)
    metodeSimson(h, fx, n)
