
from search4letters import search4letters


word = input("Podaj nazwe słowa, a my sprawdzimy czy ma samogłoski: ")

def search4vowels(word:str) -> set:
    """ This code sorts and prints vowels in a word of your preferention """
    vowels = set('aeiouy')
    return vowels.intersection(set(word))

print(search4vowels(word))