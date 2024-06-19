import matplotlib.pyplot as plt
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,13]
playing =  [8,5,7,8,3]

plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.xlabel('Day')
plt.ylabel('Hours')
plt.title('Stack Plot')
plt.legend()
plt.show()
plt.savefig('.\matplotlib\example6StackPlot.png')