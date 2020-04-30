class FSPService:
    @staticmethod
    def read_data(filepath):
        data = []
        with open(filepath) as f:
            n, m = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()[1::2]] for line in f]
        return n, m, data

    @staticmethod
    def loss_function(data, m):
        S_tmp = 0
        C_tmp = [None] * m
        for i in range(len(data[0])):
            C_tmp[i] = S_tmp + data[0][i]
            S_tmp = C_tmp[i]

        for d in data[1:]:
            S_tmp = 0
            for i in range(len(d)):
                C_tmp[i] = max(S_tmp, C_tmp[i]) + d[i]
                S_tmp = C_tmp[i]

        # S_tmp = C_tmp[m - 1] czyli Cmax, innymi słowy to początek zadania n+1
        return S_tmp


#_, m, data = FSPService.read_data('D:\Programming\python\SPD\\fsp\data\data001.txt')
#Cmax = FSPService.loss_function(data, m)
#print(Cmax)
