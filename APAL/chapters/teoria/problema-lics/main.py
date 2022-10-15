#!/usr/bin/python3

import random

def printMatrix(M):
    for line in M:
        print(" ".join([ str(_) for _ in line ]))

class MeinerLICS:
    def __init__(self):
        pass
    
    def inizializza(self, X, Y):
        self.X = X
        self.Y = Y
        self.n = len(X)
        self.m = len(Y)

        self.C = [ [ 0 for j in range(self.m+1) ] for i in range(self.n+1) ]
        self.L = [ [ (0,0) for j in range(self.m+1) ] for i in range(self.n+1) ]
        self.H = [ [ (0,0) for j in range(self.m+1) ] for i in range(self.n+1) ]
    
    def P(self, i, j):
        p = 0
        q = 0
        for w in range(1, i):
            for z in range(1, j):
                if (self.X[self.L[w][z][0] - 1] < self.X[i - 1]) and (self.C[w][z] > self.C[p][q]):
                    p,q = w,z
        return p,q

    def leggi(self):
        i,j = self.n, self.m
        Z = []

        while((i,j) != (0,0)):
            if (i,j) == self.L[i][j]:
                Z = [self.X[i-1]] + Z
                (i,j) = self.H[i][j]
            else:
                (i,j) = self.L[i][j]
        return Z

    def lics(self, X, Y):
        self.inizializza(X, Y)
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.X[i - 1] == self.Y[j - 1]:
                    (p, q) = self.P(i, j)
                    self.H[i][j] = (p, q)
                    if self.C[p][q] + 1 >= self.C[i-1][j-1]:
                        self.C[i][j] = self.C[p][q] + 1
                        self.L[i][j] = (i,j)
                    else:
                        self.C[i][j] = self.C[i-1][j-1]
                        self.L[i][j] = self.L[i-1][j-1]
                else:
                    if self.C[i][j-1] >= self.C[i-1][j]:
                        self.C[i][j] = self.C[i][j-1]
                        self.L[i][j] = self.L[i][j-1]
                    else:
                        self.C[i][j] = self.C[i-1][j]
                        self.L[i][j] = self.L[i-1][j]
        return self.leggi()

class RizziLICS:
    def __init__(self):
        pass
        
    def inizializza(self, X, Y):
        self.X = X
        self.Y = Y
        self.n = len(X)
        self.m = len(Y)
        self.Z = 0
        self.C = [ [ 0 for j in range(self.m+1) ] for i in range(self.n+1) ]
        self.H = [ [ (0,0) for j in range(self.m+1) ] for i in range(self.n+1) ]

    def leggi(self, pos):
        Z = []
        (i,j) = pos

        while((i,j) != (0,0)):
            Z = [self.X[i - 1]] + Z
            (i,j) = self.H[i][j]

        return Z

    def lics(self, X, Y):
        self.inizializza(X, Y)
        self.Zpos = (0,0)
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.H[i][j] = (0, 0)
                if self.X[i-1] != self.Y[j-1]:
                    self.C[i][j] = 0
                else:
                    max = 0
                    for h in range(1, i):
                        for k in range(1,j):
                            if self.C[h][k] > max and self.X[h - 1] < self.X[i - 1]:
                                max = self.C[h][k]
                                self.H[i][j] = (h, k)
                    self.C[i][j] = 1 + max
                    if self.C[i][j] > self.Z:
                        self.Z = self.C[i][j]
                        self.Zpos = (i, j)
        return self.leggi(self.Zpos)

DECORATORS=[MeinerLICS(), RizziLICS()]

def randomSequence(length = None):
    if (length == None):
        length = random.randint(5,30)
    return [ random.randint(1, 1000) for _ in range(length) ]

def randomCase(lengthX=None, lengthY=None):
    if (lengthX == None):
        lengthX = random.randint(5,30)
    if (lengthY == None):
        lengthY = random.randint(5,30)
    X,Y = randomSequence(lengthX), randomSequence(lengthY)
    return (X, Y)

def testCase(case):
    X,Y = case
    Z = DECORATORS[0].lics(X, Y)
    for i in range(1, len(DECORATORS)):
        W = DECORATORS[i].lics(X, Y)
        if not len(Z) == len(W):
            raise ValueError("\n".join([str(X), str(Y), f"{Z} != {W}"]))

if __name__ == "__main__":
    length = 10000
    for i in range(length):
        print(f"testing: {i} / {length}", end="\r")
        testCase(randomCase())
    print()