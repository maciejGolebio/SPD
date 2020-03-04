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
        time = sum(data[0])
        for t in range(2, len(data)):
            task = data[t]
            if time >= task[0]:
                time = time + task[1] + task[2]
            else:
                time = task[0] + task[1] + task[2]
        return time

    # data - array of data [r, p, q]
    @staticmethod
    def sort_R(data):
        order_by_access_time = data.copy()
        order_by_access_time.sort(key=lambda x: x[0])
        return order_by_access_time


n, data = RPQ.readData('D:\Programming\python\SPD\data10.txt')
inoreder = RPQ.sort_R(data)
sorted = RPQ.loss_function(inoreder)
not_sorted = RPQ.loss_function(data)
print('sort by R')
print(sorted)
print('\nnon sorted')
print(not_sorted)
