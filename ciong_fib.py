x = 0
y = 1
counter = int(input('Ile razy powtorz ciong? '))
for i in range(counter):
    print(x)
    y = y + x
    x = y - x 
    print()