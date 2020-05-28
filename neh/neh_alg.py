import copy as cp
import math

from neh.neh_service import NEHService
from fsp.fsp_service import FSPService


class NEH:
    @staticmethod
    def neh(N, m):
        k = 1
        W = [[sum(x), x] for x in N]
        pi = []
        pi_star = []
        W.sort(key=lambda x: x[0])
        while len(W) != 0:
            j = W[len(W) - 1][1]
            pi_star.append(j)
            for l in range(0, k):
                pi.insert(l, j)
                if FSPService.loss_function(pi, m) < FSPService.loss_function(pi_star, m):
                    pi_star = cp.copy(pi)
                del pi[l]
            pi = cp.copy(pi_star)
            k += 1
            del W[len(W) - 1]
        return FSPService.loss_function(pi_star, m), pi

    @staticmethod
    def select_x(pi: [], m, j):
        x = None
        C_max = math.inf
        for i in range(len(pi)):
            if pi[i] == j:
                continue
            tmp_task = pi[i]
            del pi[i]
            tmp_C_max = FSPService.loss_function(pi, m)
            if tmp_C_max < C_max:
                C_max = tmp_C_max
                x = tmp_task
            pi.insert(i, tmp_task)
        return x

    @staticmethod
    def neh_plus(N, m):
        k = 1
        W = [[sum(x), x] for x in N]
        pi = []
        pi_star = []
        W.sort(key=lambda x: x[0])
        while len(W) != 0:
            j = W[len(W) - 1][1]
            pi_star.append(j)
            for l in range(k):
                pi.insert(l, j)
                if FSPService.loss_function(pi, m) < FSPService.loss_function(pi_star, m):
                    pi_star = cp.copy(pi)
                del pi[l]
            pi = cp.copy(pi_star)
            del W[len(W) - 1]
            if k > 1:
                x = NEH.select_x(pi, m, j)
                pi.remove(x)
                for l in range(k):
                    pi.insert(l, x)
                    if FSPService.loss_function(pi, m) < FSPService.loss_function(pi_star, m):
                        pi_star = cp.copy(pi)
                    del pi[l]
                pi = cp.copy(pi_star)
            k += 1
        return FSPService.loss_function(pi_star, m), pi_star


if __name__ == '__main__':
    filepath = 'dane\\ta004.txt'
    _, m, data = NEHService.read_data_by_rows(filepath)
    C_max, pi = NEH.neh(data, m)
    print(C_max)
    print(NEH.neh_plus(data, m)[0])
