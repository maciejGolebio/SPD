import copy as cp
import data

processes = data.data.copy()
n = data.n
m = data.m

class NEH:
    @staticmethod
    def find_cmax(processes):
        start = 0;
        end = 0;
        endList = [[0 for i in range(len(processes[0]))] for j in range(len(processes))]
        startList = [[0 for i in range(len(processes[0]))] for j in range(len(processes))]
        for i in range(0, len(processes)):
            for j in range(0, len(processes[0])):
                if(i == 0):
                    start = end
                    end = start + processes[i][j]
                else:
                    if(j == 0):
                        start = endList[i-1][j]
                    else:
                        start = max(endList[i-1][j], end)
                    end = start + processes[i][j]

                startList[i][j] = start
                endList[i][j] = end
        return endList[len(processes)-1][len(processes[0])-1]

    def neh(processes):
        k = 0
        W = []
        pi = [[] for j in range(m)]
        pi2 = [[] for j in range(m)]
        tab = []
        for i in range(n):
            tmp = 0
            for j in processes:
                tmp += j[i]
                tab.insert(len(tab), j[i])
            W.append([tmp, tab.copy()])
            del tab[0:]
        W.sort(key = lambda x: x[0])
        while len(W) != 0:
            j = W[len(W) - 1][1]
            for i in range(len(j)):
                pi2[i].append(j[i])
                pi[i].append((j[i]))
            for l in range (0, k):
                if k > 0:
                    for i in range(len(j)):
                        pi2[i][k-l], pi2[i][k-l-1] = pi2[i][k-l-1], pi2[i][k-l]
                if NEH.find_cmax(pi2) < NEH.find_cmax(pi):
                    pi = cp.deepcopy(pi2)
            del W[len(W)-1]
            k += 1
        return NEH.find_cmax(pi)

print(NEH.neh(processes))