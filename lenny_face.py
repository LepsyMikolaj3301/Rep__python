lenny_str = ' 11111  00000 '
lenny = list(lenny_str)
counter = len(lenny_str)
the_j_counter = int(counter/2)
print(counter)
while(True):
    for j in range(the_j_counter):
        wena = lenny.pop(-1)
        lenny.insert(0, wena)
        print('\t',''.join(lenny))
    