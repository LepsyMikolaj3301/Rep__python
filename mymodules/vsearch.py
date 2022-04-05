
def search4vowels(word: str) -> set:
    """ This code sorts and prints vowels in a word of your preferention """
    vowels = set('aeiouy')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters:str='aeiou') -> set:
    """ This code sorts and prints letters """
    """ in a phrase of your preferention """
    return set(letters).intersection(set(phrase))
