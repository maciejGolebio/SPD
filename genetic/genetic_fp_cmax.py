import itertools as iter
import random
from neh.neh_service import NEHService
from fsp.fsp_service import FSPService
import copy as cp


def common_subseq(arr_1, arr_2):
    subseq = []
    for i in range(len(arr_1)):
        for j in range(len(arr_2)):
            if arr_1[i] == arr_2[j]:
                tmp = [arr_1[i]]
                for k in range(1, min(len(arr_1) - i, len(arr_2)) - j):
                    if arr_1[i + k] == arr_2[j + k]:
                        tmp.append(arr_1[i + k])
                    else:
                        break
                if len(tmp) > 1:
                    subseq.append(tmp)
    return subseq


class Genetic:
    def __init__(self, path_to_data, epoch):
        self.n, self.m, self.data = NEHService.read_data_by_rows(path_to_data)
        self.epoch = epoch
        self.normalizer = FSPService.loss_function(self.data, self.m) / 2

    @staticmethod
    def crossover(J1, J2) -> []:
        r = random.randint(1, len(J1) - 1)
        gens_1 = J1[:r]
        gens_2 = J2[r:]
        for i in range(min(len(gens_1), len(gens_2))):
            for j in range(min(len(gens_1), len(gens_2))):
                if gens_1[i] in gens_2[j]:
                    picker = random.randint(0, 1)
                    if picker > 0:
                        gens_1[i] = None
                    else:
                        gens_2[j] = None
            picker = random.randint(0, 1)
        if picker >= 0:
            R = J1
        else:
            R = J2
        rest = []
        for a in R:
            if (a not in gens_1) and (a not in gens_2):
                rest.append(a)

        child = gens_1 + gens_2
        for i in range(len(child)):
            if child[i] is None:
                child[i] = rest.pop()

        if None in child:
            raise Exception("bad crossover")
        return child

    @staticmethod
    def mutation(J) -> []:
        J1 = cp.copy(J)
        idx = range(len(J1))
        i, j = random.sample(idx, 2)
        J1[i], J1[j] = J1[j], J1[i]

        return J1

    @staticmethod
    def selection(population):
        """
        :param population is sorted by loss function:
        :return: parents
        """
        population.sort(key=lambda x: -x[1])
        pi = []
        acum = 0
        for i in range(len(population)):
            prev = acum
            acum += population[i][1]
            tmp = [i, prev, acum]
            pi.append(tmp)
        parents = []
        while len(parents) < 4:
            r = random.gammavariate(alpha=1.01, beta=2)
            for x in pi:
                if x[1] < r <= x[2] and population[x[0]] not in parents:
                    parents.append(population[x[0]])
        return list(iter.permutations(parents, 2))

    def calc_value(self, J):
        return 1 / (FSPService.loss_function(J, self.m) / self.normalizer)

    def generate_start_population(self, quantity):
        population = [[self.data, self.calc_value(self.data)]]
        while len(population) < quantity:
            tmp = random.sample(self.data, len(self.data))
            if tmp not in population:
                value = self.calc_value(tmp)
                population.append([tmp, value])
        return population

    def procedure(self):
        population = self.generate_start_population(self.n)

        for _ in range(self.epoch):
            new_population = [] + population
            parents = Genetic.selection(population)
            # selection
            for pair in parents:
                child = Genetic.crossover(pair[1][0], pair[0][0])
                new_population.append([child, self.calc_value(child)])
            # crossover
            random_mutation_quantity = random.randint(1, 5)
            for i in range(random_mutation_quantity):
                mutant = Genetic.mutation(random.choice(population)[0])
                new_population.append([mutant, self.calc_value(mutant)])
            new_population.sort(key=lambda x: -x[1])
            population = new_population[:len(population)]

        return FSPService.loss_function(population[0][0], self.m)


if __name__ == '__main__':
    path = "D:\\Programming\\python\\SPD\\neh\\dane\\ta012.txt"
    gen = Genetic(path, 10)

    score = gen.procedure()
    print(f'natural = {FSPService.loss_function(gen.data,gen.m)}')
    print(f'genetic = {score}')
    exit()
