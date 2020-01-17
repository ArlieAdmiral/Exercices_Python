lungime_saritura = float(input("Lungimea initiala a sariturii este "))
numar_secunde = float(input("Numarul de secunde dupa care iepurasul isi injumatateste saltul este "))
timp_total = float(input("Durata totala a deplasarii iepurasului este "))

distanta_totala = 0

while(timp_total > numar_secunde):
    distanta_totala = distanta_totala + (numar_secunde * lungime_saritura)
    lungime_saritura = lungime_saritura / 2
    timp_total = timp_total - numar_secunde
distanta_totala += (timp_total * lungime_saritura)

print("Distanta totala parcursa de iepuras este ", distanta_totala)
