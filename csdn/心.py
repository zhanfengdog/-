import math
import numpy as np
sin = np.sin 
pi = np.pi 
import matplotlib.pyplot as plt

theta=np.arange(0,2*np.pi,0.02)
ax1 = plt.subplot(121, projection='polar')
ax1.plot(theta,2*np.abs(sin(2*theta)) + np.abs(sin(4*theta)),'--',lw=2)
plt.show()