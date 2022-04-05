# Wake the fuck up samurai, we have vowels to sort...
vowels = set('aeiouy')
word = input("Podaj nazwe słowa, a my sprawdzimy czy ma samogłoski: ")
output = list(sorted(vowels.intersection(set(word))))
for i in output:
    print('znaleziona samogłoska: ', i)