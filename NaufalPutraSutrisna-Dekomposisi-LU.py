import numpy as np
import scipy.linalg as la


def Dekomposisi():
    A = np.array([[4, 3, -1], [-2, -4, 5], [1, 2, 6]])
    print("A :\n", A)
    B = np.array([[7], [5], [23]])
    print("B :\n", B)

    P, L, U = la.lu(A)
    print("L :\n", L)
    print("U :\n", U)

    Y = np.dot(np.linalg.inv(L), B)
    X = np.dot(np.linalg.inv(U), Y)
    print("Hasil Dekomposisi LU :")
    for i in range(3):
        print('X%d = %0.2f' % (i, X[i]), end='\t')


Dekomposisi()
