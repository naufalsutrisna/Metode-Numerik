def bedaMaju(f, x0, k, h):
    print("Beda Maju : ", (f(x0 + h(k)) - f(x0)) / h(k))


def bedaMundur(f, x0, k, h):
    print("Beda Mundur: ", (f(x0) - f(x0 - h(k))) / h(k))


def bedaTengah(f, x0, k, h):
    print("Beda Tengah : ", (f(x0 + h(k)) - f(x0 - h(k))) / (2 * h(k)))


def turunanKedua(f, x0, k, h):
    print("Turunan kedua : ", 1 / h(k) ** 2 * (f(x0 - h(k)) - 2 * f(x0) + f(x0 + h(k))))


if __name__ == "__main__":
    fx = lambda x: 0.1 * x ** 4 + 0.2 * x ** 3 + 0.4 * x ** 2 + 0.5 * x + 1
    x0 = 0
    k = [0, 1, 2, 3, 4]
    h = lambda x: 10 ** -x

    print("Soal ke - 1")
    for i in k:
        print("Untuk k ke -", i)
        bedaMaju(fx, x0, i, h)
        bedaMundur(fx, x0, i, h)
        bedaTengah(fx, x0, i, h)

    print("\nSoal ke - 2")
    for j in k:
        print("Untuk k ke -", j)
        turunanKedua(fx, x0, j, h)
