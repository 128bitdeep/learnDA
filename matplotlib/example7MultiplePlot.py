import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

"""Explaining 211 and 212

2 = we have two graphs
1 = 1 horizontal graph, 2 = 2 horizontal graphs
1 = first graph, 2 = second graph

211 = 2 horizontal graphs, 1 horizontal graph, 1st graph
212 = 2 horizontal graphs, 1 horizontal graph, 2nd graph

221 = 2 horizontal graphs, 2 horizontal graphs, 1st graph
222 = 2 horizontal graphs, 2 horizontal graphs, 2nd graph
"""

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()
plt.savefig('.\matplotlib\example7MultiplePlot.png')