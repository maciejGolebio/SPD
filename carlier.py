import math

from rpq_sortR import RPQ
from schrage import Schrage
from schrage_pmtn import SchragePmtn


class Carlier(SchragePmtn):

    @staticmethod
    def carlier(data):
        UB = math.inf
        Pi_star = data.copy()
        return Carlier.do_carlier(Pi_star, UB)

    @staticmethod
    def do_carlier(Pi_star, UB):
        Pi = Schrage.schrage_nlogn(Pi_star)
        U = max(RPQ.loss_function(Pi))
        if U < UB:
            UB = U
            Pi_star = Pi
        a, b, c = Carlier.find_a_b_c(Pi)
        if c is None:
            return Pi_star

        K = Carlier.find_k(Pi, c, b)
        r_ = min(K, key=lambda x: x[0])[0]
        q_ = min(K, key=lambda x: x[2])[2]
        p_ = sum(i for _, i, _ in K)

        # TODO dwie linie poniżej wrażliwe na głupte
        #######################
        H = r_ + p_ + q_
        Hc = H + sum(c)
        #######################
        tmp_r = c[0]
        c[0] = max(c[0], r_ + p_)
        LB = SchragePmtn.schrage_nlogn_pmtn(Pi_star)
        LB = max(H, Hc, LB)
        if LB < UB:
            Carlier.do_carlier(Pi_star, UB)
        c[0] = tmp_r

        #######################
        tmp_q = c[2]
        c[2] = max(c[2], q_ + p_)
        LB = SchragePmtn.schrage_nlogn_pmtn(Pi_star)
        LB = max(H, Hc, LB)
        if LB < UB:
            Carlier.do_carlier(Pi_star, UB)
        c[2] = tmp_q
        return Pi_star

    #####################################################
    ################ HELP METHODS #######################
    #####################################################

    @staticmethod
    def find_a_b_c(Pi) -> (int, int, int):
        # TODO jeżeli bugi sprawdzić wartość vs ref
        # times = list(accumulate([[0, 0, 0]] + Pi, lambda a, y: ([max(a[0], y[0]) + y[1]])))
        # times.pop(0)
        # tasks_times = list(zip(Pi, times))
        # Cmax = max(RPQ.loss_function(data))
        # b = list(map(lambda i: i[0], list((filter(lambda x: Cmax == x[1][0] + x[0][2], tasks_times)))))[-1]
        # sposob czytelniejszy niz fory ale bardziej zlozony o zipowanie

        time = 0
        Cmax = max(RPQ.loss_function(Pi))
        b = None
        for task in Pi:
            time = max(time, task[0]) + task[1]
            if time + task[2] == Cmax:
                b = task

        a = None
        p_accumulation = 0
        for task in Pi:
            p_accumulation = p_accumulation + task[1]
            if task == b:
                break

        for task in Pi:
            if Cmax == task[0] + p_accumulation + b[2]:
                a = task
                break
            p_accumulation = p_accumulation - task[1]
            if task == b:
                break

        c = None
        for task_index in range(Pi.index(a), Pi.index(b) + 1):
            if b[2] > Pi[task_index][2]:
                c = Pi[task_index]
        return a, b, c

    @staticmethod
    def find_k(Pi, c, b):
        k = []
        _from = False
        for task in Pi:
            if _from:
                # TODO Jeżeli będą bugi sprawdzić pass by refercne vs by value
                k.append(task)
            if c == task:
                _from = True
            if task == b:
                break
        return k


if __name__ == '__main__':
    tab = [10, 20, 50, 100, 200, 500]
    for i in tab:
        n, data = Carlier.read_data('D:\Programming\python\SPD\data' + str(i) + '.txt')
        Pi = Schrage.schrage_nlogn(data)
        Carlier.find_a_b_c(Pi)
        odp = Carlier.carlier(data)
        t = RPQ.loss_function(odp)
        print("carlier dla " + str(i) + ' pliku wynik to: ' + str(max(t)))
