from math import inf

from RPQ import RPQ


class Schrage:

    @staticmethod
    def read_data(filepath):
        return RPQ.readData(filepath)

    @staticmethod
    def save_min(N):
        if len(N) < 1:
            return inf
        else:
            return min(N)[0]

    @staticmethod
    def schrage(data):
        """"
                data - array of arrays [[r,p,q],[r1,p1,q1],......]
            """
        Pi = []
        k = 0
        G = []
        N = data.copy()
        t = min(N)[0]
        while len(G) != 0 or len(N) != 0:
            while len(N) != 0 and Schrage.save_min(N) <= t:
                e = min(N, key=lambda x: x[0])
                G.append(e)
                N.remove(e)

            if len(G) != 0:
                e = max(G, key=lambda x: x[2])
                G.remove(e)
                Pi.append(e)
                t = t + e[1]
                k = k + 1
            else:
                t = min(N, key=lambda x: x[0])[0]
        return Pi


tab = [10, 20, 50, 100, 200, 500]
for i in tab:
    n, data = RPQ.readData('D:\Programming\python\SPD\data' + str(i) + '.txt')
    odp = Schrage.schrage(data)
    times = RPQ.loss_function(odp)
    print('dla pliku data' + str(i) + '.txt czas to:  ' + str(max(times)))
