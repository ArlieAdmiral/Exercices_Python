import math
n = int(input("Introduceti numarul n: "))
k = 0
def prim(numar):
    if numar < 2:
        return 0
    if numar == 2:
        return 1
    for i in range(2, math.floor(numar/2)+1):
     if numar % i == 0:
            return 0
    return 1
print("Introduceti acele n numere: ")
while n:
    x = int(input())
    if prim(x) == 1:
        k += 1
    n -= 1
if k >0:
    print(k, " Dintre toate numerele introduse sunt prime, ")
else:
    print("Nu exista numere prime.")


