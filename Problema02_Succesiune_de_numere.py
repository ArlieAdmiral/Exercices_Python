n = int(input("Sa se dea n "))
ok = 1
x = []
print("Sa se dea cele n numere\n")
for i in range(0, n):
    x.append(input())
for i in range(0, n-1):
    if (int(x[i] ) % int(x[i+1] )) != 0:
        ok = 0
        break
if ok == 0:
    print("Nu toate numerele se divid succesiv ")
else:
    print("Oricare doua numere se divid succesiv intre ele ")