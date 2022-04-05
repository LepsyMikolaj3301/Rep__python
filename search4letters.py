word = input("Suggest a word: ")
the_letters = []
for i in range(5):
    the_letters.append(input("Give us please some letters to check with ;) : "))

#jak podajesz do funkcji argument, to wtedy wykorzystuje dany argument
#nawet jak jest pusty
    
def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """ This code sorts and prints letters in a phrase of your preferention """
    return set(letters).intersection(set(phrase))

print("Those values are:", search4letters(word,the_letters))