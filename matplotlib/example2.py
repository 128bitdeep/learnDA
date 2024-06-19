from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [5,8,10]
y1 = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.plot(x1,y1,'g',label='line1', linewidth=5)
plt.plot(x2,y2,'b',label='line2', linewidth=3)
plt.title("info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True,color='k')
plt.show()
plt.savefig('.\matplotlib\example2.png')