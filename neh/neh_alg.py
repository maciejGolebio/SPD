import copy as cp

from neh.neh_service import NEHService
from fsp.fsp_service import FSPService


class NEH:
    @staticmethod
    def neh(N, m):
        k = 0
        print(N)
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
                    pi_star = cp.deepcopy(pi)
                del pi[l]
            pi = cp.deepcopy(pi_star)
            k += 1
            del W[len(W) - 1]
        return FSPService.loss_function(pi_star, m), pi


if __name__ == '__main__':
    filepath = 'dane\\ta001.txt'
    _, m, data = NEHService.read_data_by_rows(filepath)
    C_max, pi = NEH.neh(data, m)
    print(C_max)
