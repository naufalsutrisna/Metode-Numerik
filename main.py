import sys
import traceback


class InterpolateNewton:
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [7.03948302, 11.2347113, 15.3418565, 19.1049999, 23.2723955,
         27.4985445, 31.6573844, 35.81462, 39.5455326, 43.4423335]

    def __init__(self):
        self.n = len(self.X)

    def compute(self):
        try:
            print("      x      y")
            result = 0
            for a in range(int(self.X[-1]) * 2 + 1):
                t = 0.5 * a
                if t == 4.5:
                    result = self.__interpolate(t)
                print("{:7.2f}{:7.2f}".format(t, self.__interpolate(t)))
            print("\nHasil dari f(4,5) adalah {:5.2f}".format(result))
        except Exception as e:
            raise

    def __interpolate(self, t):
        try:
            c = [0 for _ in range(self.n)]
            w = [0 for _ in range(self.n)]
            for i in range(0, self.n):
                w[i] = self.Y[i]
                for j in reversed(range(i)):
                    w[j] = (w[j + 1] - w[j]) / (self.X[i] - self.X[j])
                c[i] = w[0]
            s = c[self.n - 1]
            for i in reversed(range(self.n - 1)):
                s = s * (t - self.X[i]) + c[i]
            return s
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        obj = InterpolateNewton()
        obj.compute()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)