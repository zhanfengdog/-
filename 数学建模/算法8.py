def binary_search(list,item):
    low=0
    high=len(list)-1
    
    while low<=high:#循环
        mid=(low+high)
        guess=list[mid]#怎么理解
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None    
my_list=[1,3,5,6,9,13]
print(binary_search(my_list, 13))#答案是第几个  5
print(binary_search(my_list, -1))
        
        
        
        