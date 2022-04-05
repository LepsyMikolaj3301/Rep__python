
#podajemy słowo, listujemy je, sprawdzamy każdy pierwszy indeks z minusową wartością, jeśli są takie same to to palindrom

slowo = input("Podaj słowo: ")
print()

if slowo == slowo[::-1]:
    print('To slowo to palindrom!')
else:
    print("To slowo to nie palindrom!")