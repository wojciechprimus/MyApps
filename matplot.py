#I want to write an App which will make for me from collected data a plot using matplotlibrary.
#! python3
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [964,287,42,390,64,800,523]

plt.plot(x,y, label="Legenddaa")
plt.xlabel('Week')
plt.ylabel('Views')
plt.title('YouTube')
plt.legend(loc='upper center')
plt.savefig('Figure_1.png',dpi=500)
plt.show()
