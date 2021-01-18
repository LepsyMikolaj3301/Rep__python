vowels = [ 'a', 'e', 'i', 'o', 'u']
word = input("Podaj nazwe słowa, a my sprawdzimy czy ma samogłoski: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
        print(vowels)
