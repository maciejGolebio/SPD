class NEHService:
    @staticmethod
    def read_data_by_rows(filepath):
        with open(filepath) as f:
            f.readline()
            n, m = [int(x) for x in next(f).split()]
            data = [[int(x) for x in line.split()[1::2]] for line in f]
        data = list(filter(lambda x: len(x) > 1, data))
        return n, m, data


if __name__ == '__main__':
    n, m, data = NEHService.read_data_by_rows(filepath='dane\\ta001.txt')
    print(data)
