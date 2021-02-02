import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.titlesize'] = 10  #子图的标题大小
mpl.rcParams['axes.labelsize'] = 10  #子图的标签大小
mpl.rcParams['xtick.labelsize'] = 8  #横轴字体大小
mpl.rcParams['ytick.labelsize'] = 8  #纵轴字体大小
mpl.rcParams['xtick.major.size'] = 0  #x轴最大刻度大小
mpl.rcParams['ytick.major.size'] = 0  #y轴最大刻度大小

fig = plt.figure('Bar chart & Pie chart')  #整体图的标题
speed_map = {
    'dog': (48, '#7199cf'),
    'cat': (45, '#4fc4aa'),
    'cheetah': (120, '#e1a7a2')
}

#①在121位置上添加柱图，通过fig.add_subplot()加入子图
ax = fig.add_subplot(121)  
ax.set_title('Running speed - bar chart')  #子图标题
xticks = np.arange(3)  #生成x轴每个元素的位置
speeds = [x[0] for x in speed_map.values()]  #奔跑速度
bar_width = 0.5  #定义柱状图每个柱的宽度

#设置x、y轴的范围
ax.set_xlim([bar_width/2-1, 3-bar_width/2])
ax.set_ylim([0, 125])
#设置x轴标签
animals = speed_map.keys()  
ax.set_xticklabels(animals) 
ax.set_xticks(xticks)  #设置x轴上每个标签的具体位置
#设置y轴的标签
ax.set_ylabel('Speed(km/h)')  

bars = ax.bar(xticks, speeds, width=bar_width, edgecolor='none')  #设置柱的边缘为透明
colors = [x[1] for x in speed_map.values()]  #对应颜色
for bar, color in zip(bars, colors):  #给每个bar分配指定的颜色
    bar.set_color(color)
    
    
#②在122位置加入饼图
ax = fig.add_subplot(122)
ax.set_title('Running speed - pie chart')
# 生成同时包含名称和速度的标签
labels = ['{}\n{} km/h'.format(animal, speed) for animal, speed in zip(animals, speeds)]
# 画饼状图，并指定标签和对应颜色
ax.pie(speeds, labels=labels, colors=colors)
ax.axis('equal')   #保证饼图不变形
 
    
plt.savefig('Bar chart & Pie chart.png')  #保存为图片
plt.show()