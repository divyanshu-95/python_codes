from array import *
arr=array('i',[])
n=int(input('length : '))
for i in range(n):
    x=int(input('ntr the value'))
    arr.append(x)
print(arr)

del arr[2]
print('after del ',arr)
