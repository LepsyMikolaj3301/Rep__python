vowels = [ 'a', 'e', 'i', 'o', 'u']
word = input("Podaj nazwe słowa, a my sprawdzimy czy ma samogłoski: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        
for k, v  in sorted(found.items()):
        print(k , 'znaleziono', v , 'raz(y). ')
