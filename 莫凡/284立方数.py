import matplotlib.pyplot as plt

input_valub=[0,1,2,3,4,5]
cubic=[0,1,8,27,64,125]
#注意s是小写
fig,ax=plt.subplots()
#横纵参数x，y
ax.plot(input_valub,cubic,linewidth=2)#宽度
#x,y轴的范围
ax.axis([0,5,0,125])
plt.style.use('seaborn-ticks')
ax.set_title('y=x(3)',fontsize=25)
ax.set_xlabel('x',fontsize=18)
ax.set_ylabel('y',fontsize=18)
#ax.scatter(input_valub,cubic,c='red')
ax.scatter(input_valub,cubic,c=cubic,cmap=plt.cm.Greens)

#设置刻度没有=，设置补充,major是方框
ax.tick_params(axis='both',labelsize=20,which='major')

#plt.show()#第一个参数是文件名，类型，第二个是删去多余部分
plt.savefig('立方数15-1.jpg', bbox_inches='tight')


