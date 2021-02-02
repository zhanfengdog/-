import matplotlib.pyplot as plt
plt.style.use('seaborn')
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=200)

ax.set_title("square",fontsize=14)
ax.set_xlabel("X",fontsize=14)
ax.set_ylabel("Y",fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)
plt.show()