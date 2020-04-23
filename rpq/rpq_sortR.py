from timeit import default_timer as timer
from matplotlib import pyplot as plt


class RPQ:

    @staticmethod
    def readData(filepath):
        data = []
        with open(filepath) as f:
            n, kolumny = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()] for line in f]
        return n, data

    # data - array of data
    @staticmethod
    def loss_function(data):
        max_time_q = sum(data[0])
        time = data[0][0] + data[0][1]
        C = []
        for t in range(1, len(data)):
            if time > data[t][0]:
                time = time + data[t][1]
            else:
                time = data[t][0] + data[t][1]

            time_q = data[t][2] + time
            max_time_q = max(max_time_q, time_q)
            C.append(time)
        C.append(max_time_q)
        return C

    # data - array of data [r, p, q]
    @staticmethod
    def sort_R(data):
        order_by_access_time = data.copy()
        start = timer()
        order_by_access_time.sort(key=lambda x: x[0])
        end = timer()
        executionTime = end - start
        return order_by_access_time, executionTime

    @staticmethod
    def sort_R_and_Q(data):
        order = data.copy()
        start = timer()
        order.sort(key=lambda x: (x[0], x[2]))
        end = timer()
        executionTime = end - start
        # print(order)
        return order, executionTime


def main():
    tab = [10, 20, 50, 100, 200, 500]
    rTimeTab = []
    rqTimeTab = []
    for i in tab:
        n, data = RPQ.readData('data/data' + str(i) + '.txt')
        odp_r, rTime = RPQ.sort_R(data)
        odp_r_q, rqTime = RPQ.sort_R_and_Q(data)
        rTimeTab.append(rTime)
        rqTimeTab.append(rqTime)
        times_r = RPQ.loss_function(odp_r)
        times_r_q = RPQ.loss_function(odp_r_q)
        print('Sortowanie po R dla pliku data' + str(i) + '.txt czas to:  ' + str(max(times_r)))
        print('Dokonano w czasie: ' + str(rTime))
        print('Sortowanie po R i Q dla pliku data' + str(i) + '.txt czas to:  ' + str(max(times_r_q)))
        print('Dokonano w czasie: ' + str(rqTime))
    plt.plot(tab, rTimeTab)
    plt.title("R")
    plt.xlabel('data[x].txt')
    plt.ylabel('Czas [s]')

    # plt.plot(tab, rqTimeTab)
    # plt.title("RQ")
    # plt.xlabel('data[x].txt')
    # plt.ylabel('Czas [s]')

    plt.show()


if __name__ == '__main__':
    main()
