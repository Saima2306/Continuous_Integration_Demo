import pandas as pd
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
fruits = ['apple','berry','pineapple']
freq_counts = [10,52,30]

bar_labels = ['red','green','blue']
bar_color = ['tab:red','tab:green','tab:blue']

ax.bar(fruits,freq_counts,label = bar_labels,color = bar_color)
ax.set_ylabel('Supply of fruits')
ax.set_xlabel('Frequency of Different fruits')
ax.set_title('Supply of fruits with respect to different colors')
ax.legend(title = 'Fruits Supply',labels = fruits)
# plt.show()
plt.savefig('bar.png')
