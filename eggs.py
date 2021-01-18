phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)

plist2 = []

for i in range(9):
    x = plist.pop(0)
    plist2.append(x)

plist2.remove('P')
plist2.remove('a')
y = plist2.pop(2)


new_phrase = plist
plist = list(phrase)

new_phrase = ''.join(plist2)
print(plist)
print(new_phrase)
