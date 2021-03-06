import heapq
from math import inf
from timeit import default_timer as timer
from matplotlib import pyplot as plt
from rpq.rpq_sortR import RPQ
from rpq.schrage import Schrage


class SchragePmtn(Schrage):
    """
        klasa zapewnia metody pozwalające wczytać dane
        pozwalajce poszeregować zadania algorytmen schrage z przerwaniami
    """

    @staticmethod
    def loss_function(data):
        RPQ.loss_function(data)

    @staticmethod
    def schrage_pmtn(data) -> int:
        G = []
        N = data.copy()
        Cmax = 0
        t = 0
        tmp = [0, 0, inf]
        start = timer()
        while len(G) != 0 or len(N) != 0:
            while len(N) != 0 and Schrage.save_min(N) <= t:
                e = min(N, key=lambda x: x[0])
                G.append(e)
                N.remove(e)
                if e[2] > tmp[2]:
                    tmp[1] = t - e[0]
                    t = e[0]
                    if tmp[1] > 0:
                        G.append(tmp)

            if len(G) != 0:
                e = max(G, key=lambda x: x[2])
                G.remove(e)
                tmp = e
                t = t + e[1]
                Cmax = max(Cmax, t + e[2])
            else:
                t = min(N, key=lambda x: x[0])[0]
        end = timer()
        executionTime = end - start
        return Cmax, executionTime

    @staticmethod
    def schrage_nlogn_pmtn(data) -> int:
        """
         heapq sortuje po pierwszym elemncie dlatego takie udziwnie.
        N to tablica tablica krotek: [(r , [r, p,q]), (r1, [r1 ,p1 , q1]) ........]


        G analogicznie z tym że sortowane jest malejaco po q więc G = [( - q, [r, p ,q ]), ( - q1, [r1, p1, q1])  .......... ]

        :return: Cmax
        """

        N = data.copy()
        for i in range(len(data)):
            N[i] = (N[i][0], N[i])
        heapq.heapify(N)
        G = []
        t = 0
        tmp = [0, 0, inf]
        Cmax = 0
        start = timer()
        while len(G) != 0 or len(N) != 0:
            while len(N) != 0 and Schrage.save_min(N) <= t:
                e = heapq.heappop(N)
                heapq.heappush(G, (-e[1][2], e[1]))
                if e[1][2] > tmp[2]:
                    tmp[1] = t - e[1][0]
                    t = e[1][0]
                    if tmp[1] > 0:
                        heapq.heappush(G, (-tmp[2], tmp))

            if len(G) != 0:
                e = heapq.heappop(G)
                tmp = e[1]
                t = t + e[1][1]
                Cmax = max(Cmax, t + e[1][2])
            else:
                t = N[0][0]
        end = timer()
        executionTime = end - start
        return Cmax, executionTime


def main():
    tab = [10, 20, 50, 100, 200, 500]
    schragePmtnTimeTab = []
    schragePmthNlognTimeTab = []
    for i in tab:
        n, data = SchragePmtn.read_data('data/data' + str(i) + '.txt')
        odp, schrageTime = SchragePmtn.schrage_pmtn(data)
        odp2, schrageNlognTime = SchragePmtn.schrage_nlogn_pmtn(data)
        schragePmtnTimeTab.append(schrageTime)
        schragePmthNlognTimeTab.append(schrageNlognTime)
        print('Schrage: dla pliku data' + str(i) + '.txt wynik to:  ' + str(odp))
        print('Dokonano w czasie: ' + str(schrageTime))
        print('Schrage nlogn: dla pliku data' + str(i) + '.txt wynik to:  ' + str(odp))
        print('Dokonano w czasie: ' + str(schrageNlognTime))

    plt.plot(tab, schragePmtnTimeTab)
    plt.title("Schrage PMTN bez kolejki")
    plt.xlabel('data[x].txt')
    plt.ylabel('Czas [s]')

    # plt.plot(tab, schragePmthNlognTimeTab)
    # plt.title("Schrage z kolejką")
    # plt.xlabel('data[x].txt')
    # plt.ylabel('Czas [s]')

    plt.show()

if __name__ == '__main__':
    main()
