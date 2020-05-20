import copy
import math

from fsp.fsp_service import FSPService


class BruteForce:
    @staticmethod
    def find_c_max(data, m):

        def recursive(S, C_max, leaf, best, m):
            if len(S) > 0:
                for i in S:
                    s = copy.copy(S)
                    s.remove(i)
                    l = copy.copy(leaf)
                    l.append(i)
                    recursive(s, C_max, l, best, m)
            else:
                C_tmp = FSPService.loss_function(leaf, m)
                if C_max[0] > C_tmp:
                    C_max[0] = C_tmp
                    best[0] = leaf

        tmp = [math.inf]
        leafs = []
        perm = [[]]
        recursive(data, tmp, leafs, perm, m)
        return tmp[0], perm[0]


_, m, data = FSPService.read_data('D:\Programming\python\SPD\\fsp\data\data003.txt')
Cmax, perm = BruteForce.find_c_max(data, m)
print(Cmax)
print(perm)
