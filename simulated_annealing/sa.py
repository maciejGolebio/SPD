import random

from fsp.fsp_service import FSPService
import copy as cp


class SimulatedAnnealing:
    @staticmethod
    def procedure(J, n, m, L, T, reduce_temp_fcn, arg_reduce_temp, init_solution_fcn, move_fcn):
        T_end = None
        pi_new = None
        pi_star = None
        pi = init_solution_fcn(J, m)
        while T > T_end:
            for k in range(L):
                i = random.randint(0, n)
                j = random.randint(0, n)
                pi_new = move_fcn(pi, i, j)
                delta_C_max = abs(FSPService.loss_function(pi_new, m) - FSPService.loss_function(pi, m))
                if FSPService.loss_function(pi_new, m) > FSPService.loss_function(pi, m):
                    r = random.uniform(0, 1)
                    if r >= delta_C_max / T:
                        pi_new = cp.copy(pi)
                pi = pi_new
                if FSPService.loss_function(pi, m) < FSPService.loss_function(pi, m):
                    pi_star = cp.copy(pi)
            T = reduce_temp_fcn(T, arg_reduce_temp)

    @staticmethod
    def init_solution_1(J, m):
        return J

    @staticmethod
    def init_solution_2(J, m):
        pass

    @staticmethod
    def init_solution_3(J, m):
        pass

    @staticmethod
    def move_swap(Pi, i, j):
        pass

    @staticmethod
    def move_insert(Pi, i, j):
        pass

    @staticmethod
    def move_twist(Pi, i, j):
        pass

    @staticmethod
    def move_adjacent_swap(Pi, i, j):
        pass

    @staticmethod
    def reduce_temperature_linear(T):
        pass

    @staticmethod
    def reduce_temperature_geometric(T):
        pass

    @staticmethod
    def reduce_temperature_log(T):
        pass
