def count(list):
    greater=0
    for i in list:
        if i>5:
            greater+=1
            
    return greater
list=[1,2,6,7,6,2,6,8,15]
greater=count(list)
print(greater)
