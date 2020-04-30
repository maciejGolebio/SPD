import copy as cp
import numpy as np

from fsp import fsp_service


class Johnson:
    @staticmethod
    def find_cmax(data):
        l: int = 0
        k: int = len(data) - 1
        N = cp.deepcopy(data)
        Pi = [None] * (k + 1)
        while len(N) > 0:
            j, i = np.unravel_index(np.argmin(N, axis=None), np.shape(N))
            if N[j][0] < N[j][1]:
                Pi[l] = N[j]
                l = l + 1
            else:
                Pi[k] = N[j]
                k = k - 1

            del N[j]

        return Pi


_, m, data = fsp_service.FSPService().read_data('D:\Programming\python\SPD\\fsp\data\data001.txt')
Pi = Johnson.find_cmax(data)
cmax = fsp_service.FSPService.loss_function(Pi, 2)
print(Pi)
print(cmax)
