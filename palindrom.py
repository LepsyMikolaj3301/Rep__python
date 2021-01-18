
# 1. tworzymy zmienną 2. robimy liste 3. sprawdzamy czy 0 i -1 są te same i iterujemy
# x a a x
# 0 1 2 3
# -4 -3 -2 -1 

slowo = input("Napisz swoje słowo a my powiemy czy to palindrom: ")
slowko = list(slowo)
x = len(slowko)
i = 0
y = i - 1

if " " in slowko:
    slowko.remove(" ")


for i :
    if slowko[i] == slowko[y]:
        boolik = True
    else:
        boolik = False
if boolik == True:
    print("TAK")
else:
    print("NIE")