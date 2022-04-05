n = int(input("Ile liczb chcesz wprowadzic: "))
sumaUjemnych = 0
sumaDodatnich = 0

for i in range(n): 
    liczba = int(input("Podaj liczbe: "))
    if liczba < 0:
        sumaUjemnych = sumaUjemnych + liczba
    if liczba > 0:
        sumaDodatnich = sumaDodatnich + liczba

print (sumaUjemnych)
print (sumaDodatnich)