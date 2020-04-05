import sys
import itertools as it


class WiTi:

    @staticmethod
    def readData(filepath):
        data = []
        with open(filepath) as f:
            n = f.readline()
            data = [[int(x) for x in line.split()] for line in f]
        return data

    @staticmethod
    def sortD(data):
        sortedDeadlineTime = data.copy()
        sortedDeadlineTime.sort(key=lambda x: x[2])
        return sortedDeadlineTime

    @staticmethod
    def bruteForce(data):
        combination = it.permutations(data, len(data))
        F_out = sys.maxsize
        for i in list(combination):
            if WiTi.goalFunction(i) < F_out:
                F_out = WiTi.goalFunction(i)
        return F_out

    @staticmethod
    def goalFunction(data):
        # zadania
        C, F, T = [], [], []
        time = 0
        for d in data:
            time += d[0]
            C.append(time)
        F_best = 0
        for i in range(0, len(C)):
            if C[i] > data[i][2]:
                T.append(C[i] - data[i][2])
            else:
                T.append(0)
            F.append(T[i] * data[i][1])
            F_best += F[i]
        return F_best


print(WiTi.goalFunction(WiTi.readData('witiData/data10.txt')))
print(WiTi.goalFunction(WiTi.sortD(WiTi.readData('witiData/data10.txt'))))
print(WiTi.bruteForce(WiTi.readData('witiData/data10.txt')))
