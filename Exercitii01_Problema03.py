V = []
x = (input("Dati codul  "))
i = 0
while i < len(x):
    V.append(int(x[i]))
    i += 1


def dim(x):
    if len(x) <= 9:
        return 1
    return 0


def par(v):
    for i in range(1,len(v)):
        if v[i] % 2 == 0:
            return 1
    return 0


def impar(v):
    for i in range(1,len(v)):
        if v[i] % 2 == 1:
            return 1
    return 0


def f(v):
    produsPar = 1
    sumImpar = 0
    for i in range(1,len(v)):
        if v[i] % 2 == 0:
            produsPar *= i
        else:
            sumImpar += i
    if v[0] == 1:
        return 1
    elif produsPar % v[1] == sumImpar % v[1]:
        return 1
    return 0


if dim(x) == impar(V) == par(V) == f(V) == 1:
    print("\nCorect")
else:
    print("\nIncorect")
