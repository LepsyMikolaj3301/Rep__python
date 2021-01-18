word = "butelki"

for beers in range(99,0,-1):
    print(beers, word, "piwa na ścianie")
    print(beers, word, "piwa")
    print("Jedną weź")
    print("Podaj w koło.")
    if beers == 1:
        print("Nie ma już butelek piwa na ścianie")
    else:
        new_num = beers - 1
        if new_num == 1:
            word = "butelka"
        print(new_num, word, "piwa na ścianie")
    print()