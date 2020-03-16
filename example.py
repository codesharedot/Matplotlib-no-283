import numpy as np
import matplotlib.pyplot as plt

labels = ['A1', 'A2', 'A3', 'A4', 'A5']
m_means = [4,4,5,6,0]
m_std = [2, 3, 4, 1, 2]
width = 0.40       # the width of the bars

fig, ax = plt.subplots()

ax.bar(labels, m_means, width, yerr=m_std, label='Data')
ax.set_ylabel('y label')
ax.set_title('title')
ax.legend()
#plt.show()
plt.savefig('chart.png')