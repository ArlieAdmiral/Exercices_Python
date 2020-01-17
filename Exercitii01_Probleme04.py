x = int(input("Introduceti numerele: "))
precedent = x
x = int(input())
V = []
while x != -1:
    r = x - precedent
    V.append(r)
    precedent = x
    x = int(input())
bun = 3
for i in range(1, len(V)):
    if V[i] == V[i-1]:
        bun = 1
    else:
        bun = 0
        break
if bun == 1:
    print("Termenii unei progresii aritmetice")
else:
    print("Nu sunt termenii unei progresii aritmetice")