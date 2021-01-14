import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Processed.csv')
minmax = data['minmax_norm_ratings']
fig,ax = plt.subplots(figsize=(10,8))
minmax.plot(kind='hist', bins=np.arange(1,10,0.3), density=True)
minmax.plot(kind='kde')
ax.set_xlim(0,11)
ax.set_xticks(np.arange(0,11))
plt.show()