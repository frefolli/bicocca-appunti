#!/usr/bin/env python3

class MeinerLIS:
    def __init__(self):
        pass
    
    def init(self):
        self.C = [ 0 for i in range(len(self.X)+1) ]
        self.H = [ 0 for i in range(len(self.X)+1) ]
        self.L = [ 0 for i in range(len(self.X)+1) ]
        
        self.C[0:2] = [0,1]
        self.H[1] = 0
        self.L[1] = 1

    def fill(self):
        for i in range(2, len(self.X)+1):
            p = 0
            for j in range(1, i):
                if self.X[self.L[j]-1] < self.X[i-1] and self.C[j] > self.C[p]:
                    p = j
            self.H[i] = p
            if self.C[p] + 1 >= self.C[i-1]:
                self.C[i] = self.C[p]+1
                self.L[i] = i
            else:
                self.C[i] = self.C[i-1]
                self.L[i] = self.L[i-1]

    def read(self):
        i = len(self.X)
        Z = []
        while(i != 0):
            if i == self.L[i]:
                Z = [self.X[i-1]] + Z
                i = self.H[i]
            else:
                i = self.L[i]
        return Z

    def process(self, X):
        self.X = X
        self.init()
        self.fill()
        return self.read()

if __name__ == "__main__":
    X = [1,4,2,5,3]
    Z = MeinerLIS().process(X)

    print(f"X = {X}")
    print(f"Z = {Z}")