test="thit\ngg\n"
my_file=open('my file.txt','w')
my_file.write(test)

jia="我爱你"
#a为加的
my_file=open('my file.txt','a')
my_file.write(jia)
#my_file.close()

#thit gg 我爱你
file=open('my file.txt','r')
#pp=file.read()
#print(pp)

#一行行读取
#com=file.readline()
#second_read_time=file.readline()
#print(com,second_read_time
#打印出所有行['thit\n', 'gg\n']
xind=file.readlines()
print(xind)
file.close()

import pickle 
a_dict={'da':111,2:[23,1,4],'223':{1:2,'d':'sad'}}
#fole=open('pickle_example.pickle','wb')
#pickle.dump(a_dict,fole)

with open('pickle_example.pickle','rb') as fole:
    a_dict1=pickle.load(fole)
print(a_dict1)   

char_list=['a','b','c','c''d','d','e']
#找到不同的{'a', 'b', 'cd', 'c', 'd', 'e'
print(set(char_list))
#<class 'set'>
print(type(set(char_list)))
print(type({1,2}))
#空格也打印，大小写不一样{'o', 'i', 'v', 'l', 'y', ' ', 'd', 'e'}
sentense='i love lyd'
print(set(sentense))







