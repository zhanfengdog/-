import csv
from datetime import datetime
first_date=datetime.strptime('2021-1-13','%Y-%m-%d')#记得是date不是data
print(first_date)

import matplotlib.pyplot as  plt#记得加pyplot
filename='death_valley_2018_simple.csv'
with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)
        print(header_row)
        
        #for index,column_header in enumerate(header_row):
            #print(index,column_header)
        
        highs,dates,lows=[],[],[]
        for row in reader:
            current_date=datetime.strptime(row[2],'%Y-%m-%d')
            try:
                high=int(row[4])
                low=int(row[5])
            except ValueError:
                print(f"miss data for{current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
            #high=int(row[4])
            #low=int(row[5])
            #dates.append(current_date)
            #highs.append(high)
            #lows.append(low)
#print(highs) 
           
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
#中间着色，后面是alpha为深浅
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=2)


fig.autofmt_xdate()
title="2019nian"
ax.set_title(title,fontsize=24)
ax.set_xlabel(' ',fontsize=16)
ax.set_ylabel('temperature(f)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()









