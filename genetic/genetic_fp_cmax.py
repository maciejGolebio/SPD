from fsp.fsp_service import FSPService


class Genetic:
    def __init__(self, path_to_data):
        self.n, self.m, self.data = FSPService.read_data(path_to_data)
        self.population = self.generate_start_population()

    @staticmethod
    def crossover(J1, J2) -> []:
        pass

    @staticmethod
    def mutation(self, J1) -> []:
        pass

    @staticmethod
    def selection(population):
        pass

    def generate_start_population(self):
        pass


    def procedure(self):
        pass