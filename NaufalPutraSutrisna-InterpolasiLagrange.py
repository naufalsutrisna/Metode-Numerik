class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def interpolate(f: list, xi: int, n: int) -> float:
    result = 0.0
    for i in range(n):
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
        result += term
    return result


if __name__ == "__main__":
    f = [Data(1, 0.1411), Data(1.3, -0.6878), Data(1.6, -0.9962), Data(1.9, -0.5507), Data(2.2, 0.3115)]
    print("Nilai dari f(4.5) adalah {:0.2f}".format(interpolate(f, 1.5, 5)))