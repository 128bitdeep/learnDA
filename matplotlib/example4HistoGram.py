import matplotlib.pyplot as plt

popolation_ages = [22,42,55,45,12,17,19,24,82,45,96,63,36,25,48,74,58,42,75,45,12,35,64,21,19,12,18,45,47,31,22,45]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(popolation_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('Age')
plt.ylabel('Population')
plt.title('Histogram')
plt.legend()
plt.show()
plt.savefig('.\matplotlib\example4HistoGram.png')