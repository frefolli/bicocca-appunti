import time

N=10000000

def list_comprehension():
  Xs = [_ for _ in range(N)]

def for_loop():
  Xs = []
  for _ in range(N):
    Xs.append(_)

def list_map():
  Xs = list(map(lambda k: k, range(N)))

def bare_list():
  Xs = list(range(N))

def timer(F):
  S = time.time()
  F()
  E = time.time()
  print(F, E - S)

if __name__ == "__main__":
  timer(list_comprehension)
  timer(for_loop)
  timer(list_map)
  timer(bare_list)
