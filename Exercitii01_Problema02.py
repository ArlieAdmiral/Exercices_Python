import math

r = float(input("Raza cercului este "))
n = int(input("Numarul de perechi este "))

l = (r*2)/math.sqrt(2)
print("1: raza este ", r, ", latura este ", l)

for i in range(1, n):
    r = l/2
    l = (r*2)/math.sqrt(2)
    print(i+1,": raza este  ", r, ", latura este  ", l)
