#import matplotlib as plt
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)
#ax.plot(squares,linewidth=3)

ax.set_title("square",fontsize=14)
ax.set_xlabel("X",fontsize=14)
ax.set_ylabel("Y",fontsize=14)

ax.tick_params(axis='both',labelsize=14)
#ax.plot(squares)
plt.show()
