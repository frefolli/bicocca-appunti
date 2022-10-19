#!/usr/bin/python3
from fractions import Fraction

def decomposeFloat(num):
    if num < 0:
        return "-" + decomposeFloat(-num)
    elif int(num) == num:
        return str(num)
    else:
        x,y = Fraction(num).limit_denominator().as_integer_ratio()
        return f"$\\frac {x} {y}$"

class Stato:
    def __init__(self, matrix, target):
        self.matrix = matrix
        self.target = target
        self.notbase = [ _ for _ in range(1,len(self.matrix[0]) - len(self.matrix)) ]
        self.base = [ i for i in range(len(self.matrix[0]) - len(self.matrix), len(self.matrix[0]) - 1) ]
        self.it = 0

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
        self.notbase[self.notbase.index(enter)] = self.base[exit-1]
        self.base[exit-1] = enter
        multiple = 1 / self.matrix[exit][enter]
        self.matrix[exit] = [multiple * c for c in self.matrix[exit]]
        for i in range(len(self.matrix)):
            if i != exit:
                self.matrix[i] = [b - self.matrix[i][enter] * c for b,c in zip(self.matrix[i], self.matrix[exit])]

    def iteration(self):
        self.it += 1
        print("\\paragraph{iteration " + str(self.it) + "}")
        enter = self.findEnter()
        if enter == None:
            print("La prima riga non contiene piu' valori negativi, l'algoritmo del simplesso si arresta. \\\\")
            print("La soluzione di base e' " + str(self.basica()) + "\\*")
            print("La soluzione al problema PL e' " + self.normale() + "\\*")
            return False
        print(f"Scelgo la colonna {enter} perche' non esiste un coefficiente in prima riga negativo piu' basso. \\\\")
        exit = self.findExit(enter)
        if exit == None:
            print("Nessuna variabile puo' essere fatta uscire dalla base, il problema non ha soluzione ottimale.")
            raise ValueError("no variable can be pulled off of base")
        print(f"Scelgo la riga {exit} che ha il rapporto minimo. \\\\")
        print(f"Ricalcolo la tabella.")
        print(f"Questo ha l'effetto di scambiare $x_{exit}$ della base con $x_{enter}$. \\")
        self.recompute(enter, exit)
        print(self.__str__())
        return True

    def solve(self):
        print(self.__str__())
        while(self.iteration()):
            pass

    def normale(self):
        vars = [ f"$x_{self.target[i]}$" for i in range(len(self.target)) ]
        vals = []
        for i in range(len(self.target)):
            if self.target[i] in self.notbase:
                vals.append(str(0))
            else:
                for j in range(1, len(self.matrix)):
                    if self.matrix[j][self.target[i]] == 1:
                        vals.append(decomposeFloat(self.matrix[j][-1]))
                        break
        return "<" + ",".join(vars) + "> = <" + ",".join(vals) + ">"

    def basica(self):
        vars = [ f"$x_{i}$" for i in range(1,len(self.matrix[0]) - 1) ]
        vals = []
        for i in range(1,len(self.matrix[0]) - 1):
            if i in self.notbase:
                vals.append(str(0))
            else:
                for j in range(1, len(self.matrix)):
                    if self.matrix[j][i] == 1:
                        vals.append(decomposeFloat(self.matrix[j][-1]))
                        break
        return "<" + ",".join(vars) + "> = <" + ",".join(vals) + ">"

    def __str__(self):
        swrap = "\\begin{center}\n\t\\begin{tabular}{|" + "|".join([ "c" for i in range(len(self.matrix[0])) ]) + "|}"
        header = "\t\t" + " & ".join(["Z"] + [ f"$x_{i}$" for i in range(1, len(self.matrix[0]) - 1) ] + ["b"]) + "\\\\"
        rows = [ "\t\t" + " & ".join([ decomposeFloat(self.matrix[i][j]) for j in range(len(self.matrix[0])) ]) + "\\\\" for i in range(len(self.matrix)) ]
        hline = "\t\t\\hline"
        ewrap = "\t\\end{tabular}\n\\end{center}"
        return "\n".join([
            swrap, hline, header, hline] + rows + [hline, ewrap])


if __name__ == "__main__":
    MEINER = [
            [1, -1, -1,  0,  0,  0,  0,  0],
            [0,  1,  1,  1,  1,  0,  0,  2],
            [0, -1, -1, -1,  0,  1,  0, -2],
            [0,  2, -1,  0,  0,  0,  1,  0]
        ]
    
    DEINER = [
            [1, -1, -1,  0,  0,  0],
            [0,  1,  1,  1,  0,  2],
            [0,  2, -1,  0,  1,  0]
        ]
    
    print("\\section{Grosser Autobahn}")
    stato = Stato(matrix = MEINER, target = [1, 2])
    stato.solve()

    print("\\section{Kleiner Autobahn}")
    stato = Stato(matrix = DEINER, target = [1, 2])
    stato.solve()
