import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('Processed.csv')
data1 = data['mean_norm_ratings']
data2 = data['minmax_norm_ratings']
fig,ax = plt.subplots(1,1)
ax.plot(a0, color='b', label='mean norm rating')
ax.plot(b0, color='r', label= 'min-max norm rating')
ax.set_title('Distribution of mean and min-max norm ratings')
ax.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
ax.set_xlabel('mean and min-max norm rating value')
ax.set_ylabel('no. of values')
ax.legend()
plt.show()