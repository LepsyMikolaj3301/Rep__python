
word = input("Podaj nazwe słowa, a my sprawdzimy czy ma samogłoski: ")

def search4vowels(word):
    """ This is the documentation of this piece of code, it sorts and prints vowels in a word of your preferention """
    vowels = set('aeiouy')
    output = list(sorted(vowels.intersection(set(word))))
    for i in output:
        print('znaleziona samogłoska: ', i)

search4vowels(word)