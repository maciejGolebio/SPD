import copy
import math

from fsp.fsp_service import FSPService as service


class BranchAndBounds:
    @staticmethod
    def bound_1(Pi, N, m) -> int:
        max_val = -1
        E = [sum(col) for col in zip(*N)]
        for i in range(1, m + 1):
            Ci = service.loss_function(Pi, i)
            if Ci + E[i - 1] > max_val:
                max_val = Ci + E[i - 1]
        return max_val

    @staticmethod
    def bound_2(Pi, N, m, data: []) -> int:
        max_val = -1
        E = [sum(col) for col in zip(*N)]

        for i in range(1, m + 1):
            Ci = service.loss_function(Pi, i)
            sum_k = 0

            for k in range(i, m):
                min_val = math.inf
                for j in range(len(data)):
                    if data[j][k] < min_val:
                        min_val = data[j][k]
                sum_k += min_val
            if Ci + E[i - 1] + sum_k > max_val:
                max_val = Ci + E[i - 1] + sum_k

        return max_val

    @staticmethod
    def bound_3(Pi, N, m):
        max_val = -1
        E = [sum(col) for col in zip(*N)]

        for i in range(1, m + 1):
            Ci = service.loss_function(Pi, i)
            sum_k = 0
            for k in range(i, m):
                min_val = math.inf
                for j in range(len(N)):
                    if N[j][k] < min_val:
                        min_val = N[j][k]
                sum_k += min_val
            if Ci + E[i - 1] + sum_k > max_val:
                max_val = Ci + E[i - 1] + sum_k

        return max_val

    @staticmethod
    def bound_4(Pi, N, m):
        max_val = -1
        E = [sum(col) for col in zip(*N)]

        for i in range(m):
            Ci = service.loss_function(Pi, i + 1)
            min_val = math.inf
            sum_k = None
            for j in range(len(N)):
                sum_k = 0
                for k in range(i + 1, m):
                    sum_k += N[j][k]

                min_val = min(min_val, sum_k)

            if Ci + E[i] + min_val > max_val:
                max_val = Ci + E[i] + min_val

        return max_val

    @staticmethod
    def ub_1():
        return math.inf

    @staticmethod
    def ub_2(data, m):
        return service.loss_function(data, m)

    @staticmethod
    def find_c_max(data, m):
        N = copy.deepcopy(data)
        UB = [BranchAndBounds.ub_1()]
        Pi_star = [[]]

        def BnB(j, N_, Pi_):
            Pi = copy.deepcopy(Pi_)
            N = copy.deepcopy(N_)
            Pi.append(j)
            N.remove(j)
            if len(N) > 0:
                LB = BranchAndBounds.bound_4(Pi, N, m)
                pass
                if LB <= UB[0]:
                    for i in N:
                        BnB(i, N, Pi)
            else:
                Cmax = service.loss_function(Pi, m)
                if Cmax < UB[0]:
                    UB[0] = Cmax
                    Pi_star[0] = Pi

        Pi = []
        for j in N:
            BnB(j, N, Pi)

        return UB, Pi_star


if __name__ == '__main__':
    _, m, data = service.read_data('D:\Programming\python\SPD\\fsp\data\\data002.txt')
    [Cmax], [perm] = BranchAndBounds.find_c_max(data, m)
    print(Cmax)
    # Pi = [[1, 14], [10, 15]]
    # N = [[19, 5], [16, 42]]
    # tmp = BranchAndBounds.bound_2(Pi, N, 2,data)
    # print(tmp)
