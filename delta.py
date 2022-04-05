import math
print("-----------------------")
program = True
while program == True:
    print("Podaj a, b i c: ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    ac = -4*a*c
    delta = b**2 + ac
    print("Delta = ", delta)

    if delta >= 0:
        gora_x1 = -b - math.sqrt(delta)
        gora_x2 = -b + math.sqrt(delta)
        x1 = gora_x1 / (2*a)
        x2 = gora_x2 / (2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    else:
        print("Delta ujemna, brak rozwiązań!")
    
    while True:
        print('\n',"Napisz: zamknij", '\n', "Aby zakończyć program", '\n', "Napisz: dalej", '\n', "Aby obliczyc kolejny przyklad")
        wiadomosc = input()
        print()
        if "dalej" in wiadomosc:
            break
        elif "zamknij" in wiadomosc:
            program = False
            break
        elif "dalej" or "zamknij" not in wiadomosc:
            continue