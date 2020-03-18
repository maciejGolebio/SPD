from RPQ import RPQ


class Schrage:

    @staticmethod
    def read_data(filepath):
        return RPQ.readData(filepath)

    @staticmethod
    def loss_functroin():
        return 0

    @staticmethod
    def schrage(data):
        Pi = []
        k = 0
        G = []
        d = []
        N = data.copy()
        t = min(N)[0]
        while len(G) != 0 or len(N) != 0:
            while len(N) != 0 and min(N)[0] <= t:
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
                t = min(N, key=lambda x: x[0])

        return Pi


n, data = RPQ.readData('D:\Programming\python\SPD\data10.txt')

odp = Schrage.schrage(data)
print(odp)
