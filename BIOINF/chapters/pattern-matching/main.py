#!/usr/bin/env python3

def buildU(t, P):
    return [ (1 & (t == p)) for p in P ]

def moveU(X):
    Y = [1] + X[:-1]
    return Y

def andU(X, Y):
    return [ (x&y) for x,y in zip(X,Y) ]

def algoritmo(T, P):
    n,m = len(T), len(P)
    M = []
    M.append(buildU(T[0], P))
    for j in range(1, n):
        U = moveU(M[-1])
        V = buildU(T[j], P)
        M.append(andU(U, V))
    return transpose(M)

def transpose(M):
    n,m = len(M), len(M[0])
    return [ [ M[i][j] for i in range(n) ] for j in range(m) ]

def stampa(matrice):
    for line in matrice:
        print(" ".join([ str(_) for _ in line ]))

if __name__ == "__main__":
    T = "abracadabra"
    P = "abr"
    print(f'T = {T}')
    print(f'P = {P}')
    stampa(algoritmo(T, P))
