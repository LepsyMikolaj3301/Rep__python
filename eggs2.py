phrase = input("Podaj nazwe: ")
plist = list(phrase)
print(phrase)
print(plist)

plist2 = []
plist2.extend(plist[1:3])
plist2.extend(plist[5:9])
plist = plist2

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

