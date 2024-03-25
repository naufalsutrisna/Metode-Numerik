import numpy as np
import matplotlib.pyplot as plt


def diagram():
    x_points = np.arange(3, 6, 0.01);
    y_points = np.sin(10 * x_points) + np.cos(3 * x_points)
    plt.plot(x_points, y_points, color='hotpink')
    plt.title('Metode Biseksi')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()


diagram()


def biseksi(fx):
    try:
        a = float(input("Masukkan nilai a : "))
        afinal = a
        b = float(input("Masukkan nilai b : "))
        bfinal = b
        c = a
        if fx(a) * fx(b) < 0:
            print("a\t\tb\t\tfx(a)\tfx(b)\tc\t\tfx(c)\tgalat")
            while (True):
                cp = c
                c = (a + b) / 2
                galat = abs((c - cp) / c)
                print(f'{a:.3f}\t{b:.3f}\t{fx(a):.3f}\t{fx(b):.3f}\t{c:.3f}\t{fx(c):.3f}\t{galat:.3f}')
                if fx(a) * fx(c) > 0:
                    a = c
                else:
                    b = c
                if galat < 0.005:
                    break
            print(f'Akar persamaan dari nilai rentang {afinal} dan {bfinal} adalah {c:.3f}')
        else:
            print("Harap masukkan kembali!")
            biseksi(fx)
    except:
        print("Mohon Masukkan Hanya angka saja!")
        biseksi(fx)


fx = lambda x: np.sin(10 * x) + np.cos(3 * x)
biseksi(fx)