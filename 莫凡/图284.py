import matplotlib.pyplot as plt
x_values=range(1, 1001)
y_values=[x**2 for x in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=20,c='green')
#渐变色一定要大写
ax.scatter(x_values,y_values,c=y_values,s=20,cmap=plt.cm.Blues)


ax.set_title("square",fontsize=14)
ax.set_xlabel("X",fontsize=14)
ax.set_ylabel("Y",fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)
#x轴的范围，y轴的范围
ax.axis([0,1200,0,1100000])
plt.show()