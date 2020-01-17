import math

a = float(input("Lungimea primei laturi "))
b = float(input("Lungimea celei de-a doua laturi "))
c = float(input("Lungimea celei de-a treia laturi "))


def echilateral():
    if a == b == c:
        return 1
    return 0


def isoscel():
    if a == b and a != c and b != c:
        return 1
    if b == c and b != a and c != a:
        return 1
    if a == c and a != b and a != c:
        return 1
    return 0


def dreptunghic():
    if a*a + b*b == c*c:
        return 1
    if b*b + c*c == a*a:
        return 1
    if a*a + c*c == b*b:
        return 1
    return 0


print("\nTriunghiul este ")
if dreptunghic():
    print("dreptunghic ")
elif isoscel():
    print("isoscel")
elif echilateral():
    print("echilateral")
else:
    print("oarecare")


p = (a + b + c)/2    #semiperimetrul
A = math.sqrt(p * (p - a) * (p - b) * (p - c))   #aria triunghiului
print("\nAria triunghiului este ", A)

print("\nLungimea inaltimii laturii a este ", 2 * A / a)
print("Lungimea inaltimii laturii b este ", 2 * A / b)
print("Lungimea inaltimii laturii c este ", 2 * A / c)