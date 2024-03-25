import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, e):
    if not (f(a) * f(b) < 0):
        raise Exception(
            "Nilai a dan b tidak memenuhi syarat, akar yang dicari tidak berada di antara a dan b!")

    print("i", "\t", "a", "\t", "b", "\t", "f(a)", "\t",
          "f(b)", "\t", "c", "\t", "f(c)")
    i = 0
    c = (a + b) / 2
    while abs(f(c)) > e:
        i += 1
        print(i, "\t", round(a, 3), "\t", round(b, 3), "\t", round(f(a), 3), "\t",
              round(f(b), 3), "\t", round(c, 3), "\t", round(f(c), 6))
        if f(a) * f(c) < 0:
            b = c
        elif f(a) * f(c) > 0:
            a = c
        c = (a + b) / 2
    print(f"nilai akar persamaan menggunakan bisection adalah {c}")


if __name__ == "__main__":
    fx = lambda x: x ** 2 + 5 * x - 6
    x1 = -10
    x2 = 10
    e = 0.00001
    bisection(fx, x1, 0, e)
    bisection(fx, 0, x2, e)

    x_points = np.arange(x1, x2, 0.01);
    y_points = x_points ** 2 + 5 * x_points - 6
    plt.plot(x_points, y_points, color='navy')
    plt.title('Grafik fungsi x^2 + 5x - 6')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
