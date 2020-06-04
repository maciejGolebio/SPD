import math
import numpy as np
import random

from fsp.fsp_service import FSPService
from neh.neh_service import NEHService
import copy as cp


class SimulatedAnnealing:
    @staticmethod
    def procedure(J, n, m, L, T, reduce_temp_fcn, arg_reduce_temp, init_solution_fcn, move_fcn):
        T_end = 0.05
        pi_new = None
        pi_star = init_solution_fcn(J, m)
        pi = init_solution_fcn(J, m)
        while T > T_end:
            for k in range(L):
                i = random.randint(0, n - 1)
                j = random.randint(0, n - 1)
                pi_new = move_fcn(pi_star, i, j)
                delta_C_max = FSPService.loss_function(pi, m) - FSPService.loss_function(pi_new, m)
                if delta_C_max > 0:
                    r = random.uniform(0, 1)
                    if r >= np.e ** (delta_C_max / T):
                        pi_new = cp.copy(pi)
                pi = pi_new
                if FSPService.loss_function(pi, m) < FSPService.loss_function(pi_star, m):
                    pi_star = cp.copy(pi)
            T = reduce_temp_fcn(T, arg_reduce_temp)
        print(FSPService.loss_function(pi, m))

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
        Pi[i], Pi[j] = Pi[j], Pi[i]
        return Pi

    @staticmethod
    def move_insert(Pi, i, j):
        pass

    @staticmethod
    def move_twist(Pi, i, j):
        pass

    @staticmethod
    def move_adjacent_swap(Pi, i, j):
        """
        :param Pi:
        :param i: <0,len(Pi)-2>
        :param j: -------------
        :return: better neighbour
        """
        pass

    @staticmethod
    def reduce_temperature_linear(T, x):
        return T - x

    @staticmethod
    def reduce_temperature_geometric(T, alpha):
        return T * alpha

    @staticmethod
    def reduce_temperature_log(T, it):
        b = it + 1
        return T / np.log(b)


if __name__ == '__main__':
    filepath = 'D:\Programming\python\SPD\\neh\dane\\ta003.txt'
    n, m, data = NEHService.read_data_by_rows(filepath)
    natural_c_max = FSPService.loss_function(data, m)
    print(f'natural Cmax = {natural_c_max}')
    L = [10 ** 2, 10 ** 3, 10 ** 4]
    T_0 = [math.sqrt(n), n, n ** 2]
    temp_reduce_fcn_arr = [SimulatedAnnealing.reduce_temperature_linear,
                           SimulatedAnnealing.reduce_temperature_geometric,
                           SimulatedAnnealing.reduce_temperature_log]
    x = [T_0[0] / (10 ** 3), T_0[0] / (10 ** 4), T_0[0] / (10 ** 5)]
    alpha = [.97, .95, .9]
    init_solution_fcn_arr = [SimulatedAnnealing.init_solution_1,
                             SimulatedAnnealing.init_solution_2,
                             SimulatedAnnealing.init_solution_3]
    move_fcn_arr = [SimulatedAnnealing.move_swap,
                    SimulatedAnnealing.move_insert,
                    SimulatedAnnealing.move_twist,
                    SimulatedAnnealing.move_adjacent_swap]
    SimulatedAnnealing.procedure(data, n, m,
                                 L[0],
                                 T_0[1],
                                 temp_reduce_fcn_arr[0],
                                 x[0],
                                 init_solution_fcn_arr[0],
                                 move_fcn_arr[0])
