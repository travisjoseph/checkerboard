def getChar(sc, i, j, cs):
    return chr(sc+((i+j)%cs))

sc = 'a'
cs = 4
row = 5
column = 6

for r in range(row):
    for c in range(column):
        print(getChar(ord(sc), c, r, cs), end='')
    print("")



