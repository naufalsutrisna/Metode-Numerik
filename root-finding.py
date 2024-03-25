def bisection(f, a, b, e):
    if not (f(a) * f(b) < 0):
        raise Exception(
            "Nilai a dan b tidak memenuhi syarat, akar yang dicari tidak berada di antara a dan b!")

    print("i", "\t", "a", "\t", "b", "\t", "f(a)", "\t",
          "f(b)", "\t", "c", "\t", "f(c)")
    i = 0
    c = (a + b)/2
    while (abs(f(c)) > e):
        i += 1
        print(i, "\t", round(a, 3), "\t", round(b, 3), "\t", round(f(a), 3), "\t",
              round(f(b), 3), "\t", round(c, 3), "\t", round(f(c), 6))
        if (f(a) * f(c) < 0):
            b = c
        elif (f(a) * f(c) > 0):
            a = c
        c = (a + b)/2
    print(f"nilai akar persamaan menggunakan bisection adalah {c}")


def bisection_recursive(f, a, b, e, i):
    if not (f(a) * f(b) < 0):
        raise Exception(
            "Nilai a dan b tidak memenuhi syarat, akar yang dicari tidak berada di antara a dan b!")

    i += 1
    c = (a + b)/2
    print(i, "\t", round(a, 3), "\t", round(b, 3), "\t", round(f(a), 3), "\t",
          round(f(b), 3), "\t", round(c, 3), "\t", round(f(c), 6))

    if abs(f(c)) < e:
        return c
    else:
        if (f(a) * f(c) < 0):
            b = c
        else:
            a = c
        return bisection_recursive(f, a, b, e, i)


def false_pos(f, a, b, e):
    if not (f(a) * f(b) < 0):
        raise Exception(
            "Nilai a dan b tidak memenuhi syarat, akar yang dicari tidak berada di antara a dan b!")

    print("i", "\t", "a", "\t", "b", "\t", "f(a)", "\t",
          "f(b)", "\t", "c", "\t", "f(c)")
    i = 0
    c = b - ((f(b)*(b-a))/(f(b)-f(a)))
    #c = a - ((fx(a)*(a-b))/(fx(a)-fx(b)))
    while (abs(f(c)) > e):
        i += 1
        print(i, "\t", round(a, 3), "\t", round(b, 3), "\t", round(f(a), 3), "\t",
              round(f(b), 3), "\t", round(c, 3), "\t", round(f(c), 6))
        if (f(a) * f(c) < 0):
            b = c
        elif (f(a) * f(c) > 0):
            a = c
        c = b - ((f(b)*(b-a))/(f(b)-f(a)))
        #c = a - ((fx(a)*(a-b))/(fx(a)-fx(b)))
    print(f"nilai akar persamaan menggunakan False-Position adalah {c}")


def false_pos_recursive(f, a, b, e, i):
    if not (f(a) * f(b) < 0):
        raise Exception(
            "Nilai a dan b tidak memenuhi syarat, akar yang dicari tidak berada di antara a dan b!")

    i += 1
    c = b - ((f(b)*(b-a))/(f(b)-f(a)))
    #c = a - ((fx(a)*(a-b))/(fx(a)-fx(b)))
    print(i, "\t", round(a, 3), "\t", round(b, 3), "\t", round(f(a), 3), "\t",
          round(f(b), 3), "\t", round(c, 3), "\t", round(f(c), 6))

    if abs(f(c)) < e:
        return c
    else:
        if (f(a) * f(c) < 0):
            b = c
        else:
            a = c
        return false_pos_recursive(f, a, b, e, i)


def nr(f, df, x0, e):
    print("i", "\t", "x", "\t", "f(x)")
    i = 1
    print(i, "\t", round(x0, 3), "\t", round(f(x0), 6))
    while (abs(f(x0)) > e):
        i += 1
        x0 = x0 - f(x0)/df(x0)
        print(i, "\t", round(x0, 3), "\t", round(f(x0), 6))
    print(f"nilai akar persamaan menggunakan Newton-Raphson adalah {x0}")

def nr_recursive(f, df, x0, e, i):
    i += 1
    print(i, "\t", round(x0, 3), "\t", round(f(x0), 6))
    if abs(f(x0)) < e:
        return x0
    else:
        return nr_recursive(f, df, x0 - f(x0)/df(x0), e, i)

def secant(f, x0, x1, e):
    print("i", "\t", "x", "\t", "f(x)")
    i = 1
    print(i, "\t", round(x1, 3), "\t", round(f(x1), 6))
    while (abs(f(x1)) > e):
        i += 1
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x
        print(i, "\t", round(x1, 3), "\t", round(f(x1), 6))
    print(f"nilai akar persamaan menggunakan Secant adalah {x1}")

def secant_recursive(f, x0, x1, e, i):
    i += 1
    y = f(x1)
    print(i, "\t", round(x1, 3), "\t", round(y, 6))
    if abs(y) < e:
        return x1
    else:
        return secant_recursive(f, x1, x1 - f(x1)*(x1-x0)/(f(x1)-f(x0)), e, i)

if __name__ == "__main__":
    f = lambda x: x**3 - 2*(x**2) + 6*x - 4
    df = lambda x: 3*x**2 - 4*x + 6
    x0 = -10
    x1 = 10
    a = 0
    b = 10
    e = 10e-6
    bisection(f, a, b, e)
    print(f"nilai akar persamaan menggunakan Bisection secara rekursi adalah{bisection_recursive(f, a, b, e, 0)}")
    false_pos(f, a, b, e)
    print(f"nilai akar persamaan menggunakan False-Position secara rekursi adalah{false_pos_recursive(f, a, b, e, 0)}")
    nr(f, df, x0, e)
    print(f"nilai akar persamaan menggunakan Newton-Raphson secara rekursi adalah {nr_recursive(f, df, x0, e, 0)}")
    secant(f, x0, x1, e)
    print(f"nilai akar persamaan menggunakan Secant secara rekursi adalah {secant_recursive(f, x0, x1, e, 0)}")
