#!/usr/bin/python3

class Stato:
    def __init__(self, matrix, target, base):
        self.matrix = matrix
        self.target = target
        self.base = base

    def findEnter(self):
        min = None
        for n in self.target:
            if self.matrix[0][n] < 0:
                if min == None or self.matrix[0][n] < self.matrix[0][min]:
                    min = n
        return min
    
    def findExit(self, enter):
        min = None
        for i in range(1, len(self.matrix)):
            if self.matrix[i][enter] > 0 and self.matrix[i][-1] >= 0:
                if min == None or (self.matrix[i][-1] / self.matrix[i][enter]) < (self.matrix[min][-1] / self.matrix[min][enter]):
                    min = i
        return min

    def recompute(self, enter, exit):
        multiple = 1 / self.matrix[exit][enter]
        self.matrix[exit] = [multiple * c for c in self.matrix[exit]]
        for i in range(len(self.matrix)):
            if i != exit:
                self.matrix[i] = [b - self.matrix[i][enter] * c for b,c in zip(self.matrix[i], self.matrix[exit])]

    def iteration(self):
        enter = self.findEnter()
        if enter == None:
            return False
        exit = self.findExit(enter)
        if exit == None:
            raise ValueError("no variable can be pulled off of base")
        self.recompute(enter, exit)
        print(self.__str__())
        print("#########################")
        return True

    def solve(self):
        print("#########################")
        print(self.__str__())
        print("#########################")
        while(self.iteration()):
            pass

    def __str__(self):
        return "\n".join([ " ".join([str(self.matrix[j][i]) for i in range(len(self.matrix[j]))]) for j in range(len(self.matrix))])

if __name__ == "__main__":
    stato = Stato(matrix = [
            [1, -1, -1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 2],
            [0, -1, -1, -1, 0, 1, 0, -2],
            [0, 2, -1, 0, 0, 0, 1, 0]
        ], target = [1, 2], base = [1,2,3])
    stato.solve()
