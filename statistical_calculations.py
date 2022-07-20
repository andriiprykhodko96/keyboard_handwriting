from math import sqrt

Tt = 2.2622 # n-1 = 9
Ft = 3.18   # n-1 = 9

def expected_value(X):
    return sum(X) / len(X)

def variance(X, M):
    S = 0
    for x in X:
        S += (x - M) ** 2
    S /= len(X) - 1
    S = sqrt(S)
    return S

def without(X, index):
    return [X[i] for i in range(len(X)) if i != index]

def Student_coefficient(X, xi):
    M = expected_value(X)
    S = variance(X, M)
    tp = abs((xi - M) / S)
    return tp

def remove_brute_errors(X):
    correct = []
    for i in range(len(X)):
        tp = Student_coefficient(without(X, i), X[i])
        if tp <= Tt:
            correct.append(X[i])
    return correct

def Fisher_coefficient(Smin, Y):
    Smax = variance(Y, expected_value(Y))
    if Smin > Smax:
        Smin, Smax = Smax, Smin
    Fp = Smax / Smin
    return Fp <= Ft

def equal_center(Mx, Sx, Y):
    My = expected_value(Y)
    Sy = variance(Y, My)
    n = len(Y)
    S = sqrt((Sx ** 2 + Sy ** 2) * (n - 1) / (2 * n - 1))
    tp = abs(Mx - My) / (S * sqrt(2 / n))
    return tp <= Tt
