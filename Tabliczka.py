import random

#co do roboty
# 2 zmienne od różnych randomów od 1 do 10 które się mnożą i 5 prób dla gracza 
# licz każde dobre rozwiązanie i zrób konkluzje
#

wspol = 0

for i in range(5):
    x = random.randint(1,10)
    y = random.randint(1,10)

    print("Ile to: ", x , " * " , y)
    wynik = input("Wynik: ")
    wynik = int(wynik)
    
    if wynik == x*y:
        print("WSPANIALE! ODPOWIEDŹ POPRAWNA!")
        wspol = wspol + 1
    elif wynik != x*y:
        print("ODPOWIEDŹ NIEPOPRAWNA!")
        print("SPRÓBUJ SWOICH SIŁ W NASTĘPNYM PRZYKŁADZIE!")
        print("POPRAWNY WYNIK:" , x*y)
    elif wynik == 69:
        print('\t', "NICE")
        print('\t', '( ͡° ͜ʖ ͡°)')
    print()

print("Zobaczmy jak ci poszło!")

if wspol <= 1:
    print("Tabliczka mnożenia nie idzie ci za dobrze :( ")
    print("Następnym razem będzie lepiej ;)")
    print("Miałeś:", wspol, "/ 5")
elif wspol <= 3:
    print("Mniej więcej znasz tabliczka mnożenia, ale mogło być lepiej!")
    print("Miałeś:", wspol, "/ 5")
elif wspol <= 5:
    print("ZNAKOMICIE znasz tabliczkę mnożenia! BRAWO!")
    print("Miałeś:", wspol, "/ 5")
