from timeit import default_timer as timer

def readData(filepath):
    with open(filepath) as f:
        n, columns = [int(x) for x in next(f).split()]
        data = [[int(x) for x in line.split()] for line in f]
    return n, data


def configureBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def recursiveDynamic(I, d, F):
    binaryValue = bin(I).replace("0b", "")
    maxValueTab = []
    for i in range(0, len(binaryValue)):
        configuredBit = configureBit(I, i, 0)
        configuredBitBinary = bin(configuredBit).replace("0b", "")
        reversedStr = ''.join(reversed(binaryValue))
        p = [pos for pos, char in enumerate(reversedStr) if char == '1']
        if binaryValue != configuredBitBinary:
            ile = 0
            for m in range(0, len(p)):
                ile += d[p[m]][0]
            current_F = F[configuredBit]
            if current_F == -1:
                current_F = recursiveDynamic(configuredBit, d, F)
            maxValue = max(ile - d[i][2], 0) * d[i][1] + current_F
            maxValueTab.append(maxValue)
    minValue = min(maxValueTab)
    F[I] = minValue
    return minValue


def loopDynamic(n, d):
    F = []
    maxValueTab = []
    start = timer()
    F.append(max(d[0][0] - d[0][2], 0) * d[0][1])
    for i in range(1, 2 ** n):
        binaryValue = bin(i).replace("0b", "")
        for j in range(0, len(binaryValue)):
            configuredBit = configureBit(i, j, 0)
            configuredBitBinary = bin(configuredBit).replace("0b", "")
            reversedStr = ''.join(reversed(binaryValue))
            p = [pos for pos, char in enumerate(reversedStr) if char == '1']
            if binaryValue != configuredBitBinary:
                ile = 0
                for m in range(0, len(p)):
                    ile += d[p[m]][0]
                maxValue = max(ile - d[j][2], 0) * d[j][1] + F[configuredBit]
                maxValueTab.append(maxValue)
        minValue = min(maxValueTab)
        F.append(minValue)
        maxValueTab = []
    end = timer()
    result = end - start
    print("Loop - wynik:", F.pop())
    print("Loop - czas wykonania:", result)
    return F.pop()


def main():
    loop = []
    recursive = []
    data = ['witiData/data10.txt', 'witiData/data11.txt', 'witiData/data12.txt', 'witiData/data13.txt', 'witiData/data14.txt', 'witiData/data15.txt', 'witiData/data16.txt', 'witiData/data17.txt', 'witiData/data18.txt', 'witiData/data19.txt', 'witiData/data20.txt']
    result = 0
    for j in range(3):
        print("PODEJŚCIE", j+1)
        for d in data:
            print(str(d))
            n, d = readData(d)
            loop.append(loopDynamic(n, d))
            F = [0]
            for i in range(0, 2 ** n - 1):
                F.append(-1)
            I = 2 ** n - 1
            start = timer()
            recursiveDynamic(I, d, F)
            end = timer()
            result = end - start
            print("Recursive - wynik: ", F.pop())
            print("Recursive - czas wykonania: ", result)
            recursive.append(F.pop())
    print(loop)
    print(recursive)

if __name__ == '__main__':
    main()
