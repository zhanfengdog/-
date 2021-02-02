import akshare as ak
import pandas as pd
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

df = ak.stock_zh_a_daily(symbol="sz002241", start_date="20200101", end_date="20210115",
                         adjust="qfq")
df.to_excel("歌尔股份year.xlsx")
df = pd.read_excel("歌尔股份year.xlsx")
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
df["SMA20"]=df["close"].rolling(20).mean()
df["SMA30"]=df["close"].rolling(30).mean()
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(df["date"],df["SMA20"])
ax.plot(df["date"],df["SMA30"])
ax.xaxis.set_major_locator(ticker.MaxNLocator(20))
def format_date(x, pos=None):
    if x < 0 or x > len(df['date']) - 1:
        return ''
    return df['date'][int(x)]
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()