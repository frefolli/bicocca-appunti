import matplotlib.pyplot

K=1000
M=1000*K

values = [
  6*K,
  552,
  1*K,
  14*K,
  148*K
]

values = sorted(values)
matplotlib.pyplot.plot(range(len(values)), values, label='LoC', marker='o')
matplotlib.pyplot.savefig('locs.png')
matplotlib.pyplot.close()
