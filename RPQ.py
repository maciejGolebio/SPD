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
        order_by_access_time.sort(key=lambda x: x[0])
        return order_by_access_time

    @staticmethod
    def sort_R_and_Q(data):
        order = data.copy()
        order.sort(key=lambda x: [x[0], x[2]])
        # print(order)
        return order


def main():
    tab = [10, 20, 50, 100, 200, 500]
    for i in tab:
        n, data = RPQ.readData('D:\Programming\python\SPD\data' + str(i) + '.txt')
        odp_r = RPQ.sort_R(data)
        odp_r_q = RPQ.sort_R_and_Q(data)
        times_r = RPQ.loss_function(odp_r)
        times_r_q = RPQ.loss_function(odp_r_q)
        print('Sortowanie po R dla pliku data' + str(i) + '.txt czas to:  ' + str(max(times_r)))
        print('Sortowanie po R i Q dla pliku data' + str(i) + '.txt czas to:  ' + str(max(times_r_q)))


if __name__ == '__main__':
    main()
