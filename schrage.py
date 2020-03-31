from math import inf
from timeit import default_timer as timer
from matplotlib import pyplot as plt
from rpq_sortR import RPQ
import heapq



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
        G = []
        N = data.copy()
        t = min(N)[0]
        start = timer()
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
            else:
                t = min(N, key=lambda x: x[0])[0]
        end = timer()
        executionTime = end - start
        return Pi, executionTime

    @staticmethod
    def schrage_nlogn(data):
        """"
            " heapq is a binary heap, with O(log n) push and O(log n) pop. " - dokumentacja
        """
        N = data.copy()
        for i in range(len(data)):
            N[i] = (N[i][0], N[i])
        heapq.heapify(N)
        """"
               mozna to zaltwic przy wczytaniu danych nie wplywa na zloznosc samego algorytmu
               
               N to tablica tablica krotek takich że (r , [r, p,q]), (r1, [r1 ,p1 , q1]) ........
               heapq sortuje po pierwszym elemncie dlatego tak
               
               G analogicznie z tym że sortowane jest malejaco po q więc G = [(q, [r, p ,q ]), (q1, [r1, p1, q1])  .......... ] 
        """
        G = []
        Pi = []
        t = N[0][0]
        start = timer()
        while len(G) != 0 or len(N) != 0:
            while len(N) != 0 and Schrage.save_min(N) <= t:
                e = heapq.heappop(N)
                heapq.heappush(G, (-e[1][2], e[1]))  # O(log n)
            if len(G) != 0:
                e = heapq.heappop(G)  # O(log n)
                Pi.append(e[1])  # O(1)
                t = t + e[1][1]
            else:
                t = N[0][0]  # O(1)
        end = timer()
        executionTime = end - start
        return Pi, executionTime


def main():
    tab = [10, 20, 50, 100, 200, 500]
    schrageTimeTab = []
    schrageNlognTimeTab = []
    for i in tab:
        n, data = RPQ.readData('data/data' + str(i) + '.txt')
        n1, data1 = RPQ.readData('data/data' + str(i) + '.txt')
        odp, schrageTime = Schrage.schrage(data)
        odp1, schrageNlognTime = Schrage.schrage_nlogn(data)
        schrageTimeTab.append(schrageTime)
        schrageNlognTimeTab.append(schrageNlognTime)
        times = RPQ.loss_function(odp)
        times1 = RPQ.loss_function(odp1)
        print('dla pliku data na tablicy' + str(i) + '.txt wynik to:  ' + str(max(times)))
        print('Dokonano w czasie: ' + str(schrageTime))
        print('dla pliku data na kopcu' + str(i) + '.txt wynik to:  ' + str(max(times1)))
        print('Dokonano w czasie: ' + str(schrageNlognTime))

    plt.plot(tab, schrageTimeTab)
    plt.title("Schrage bez kolejki")
    plt.xlabel('data[x].txt')
    plt.ylabel('Czas [s]')

    # plt.plot(tab, schrageNlognTimeTab)
    # plt.title("Schrage z kolejką")
    # plt.xlabel('data[x].txt')
    # plt.ylabel('Czas [s]')

    plt.show()

if __name__ == '__main__':
    main()
    # n, data = RPQ.readData('D:\Programming\python\SPD\data200.txt')
    # c = Schrage.schrage_nlogn(data)
    # time = RPQ.loss_function(c)
    # print(str(max(time)))
    # print(c)
