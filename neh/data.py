filepath = 'dane/ta001.txt'

with open(filepath) as fp:
    ignoredFirstLine = " ".join(fp.readline().split())
    firstLine = " ".join(fp.readline().split())

    # added parameters from file
    firstLineWithNM = firstLine.split()
    n = int(firstLineWithNM[0])
    m = int(firstLineWithNM[1])

    tmp1 = []
    tmp2 = []
    for i in range (n):
        tmp2.append([int(m) for m in fp.readline().split()])

    for i in range (n):
        new = []
        for j in range(1, len(tmp2[0]), 2):
            new.append(tmp2[i][j])
        tmp1.append(new)

data = [[0 for i in range(n)] for j in range(m)]

for i in range(n):
    for j in range(m):
        data[j][i] = tmp1[i][j]