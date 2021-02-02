text='身高:178,tizhong:168,num:76,mima:123'
target='168'
if target in text:
    print("找到了，真棒")
print(text.index(target))   
 
import re
wen='123,455,520,222,12-35,shengao,身高,2356,123-32'
print(re.findall(r'123', wen))  #['123', '123']
#找出一个数字
print(re.findall(r'\d' , wen)) 
#非数字，标点
print(re.findall(r'\D' , wen))  
#1之三，加‘’
print(re.findall(r'[1-3]' , wen))
#['身高']
print(re.findall(r'身高' , wen)) 
#['身', '高'] 
print(re.findall(r'[身高]' , wen))
#['s', 'h', 'e', ]
print(re.findall(r'[a-z]' , wen))
#['55', '5']
print(re.findall(r'5+' , wen)) 
 #0个数字或多个 
#print(re.findall(r'\d*' , wen)) 
print(re.findall(r'\d{3}' , wen)) #['123', '455']
print(re.findall(r'\d{4,5}' , wen)) #['12355']
#四个数字以上的
print(re.findall(r'\d{4,}' , wen))
#['12-35', '123-32']
print(re.findall(r'\d{2,3}-\d{2}',wen))
#\表示一个字符
xin='18320642421,1235-321,73251,5678-456'
print(re.findall(r'^1\d{10}|^\d{4}-\d{3}',xin))
#print(re.findall(r'$1\d{10}|$\d{4}-\d{3}',xin))


test='barbar carcar harhel,12'
#(\1)与第一个括号相同
print(re.findall(r'(\w{3})(\1)',test))
#不包含空格 
print(re.findall(r'\w',test))
 #两个空格[范围]{次数}[^3-8]非3到8都行
print(re.findall(r'\s(?#注释)',test))

testa='lyd,Lyd,LYD'
#忽略大小写
print(re.findall(r'lyd',testa,flags=re.I))

#像打游戏一样学编程
#①查找
#search-只返回1个，match只返回1个，从头开始匹配
#findall-返回所有的字符串 finditersga返回Match迭代器
#②替换
#sub替换字符 subn替换后且告诉我有几个字符被替换
#③分割split














