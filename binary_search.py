#all values in sorted
pos=-1

def search(lis,n):
    l=0
    u=len(lis-1)
    while l <= u:
        mid=(l+u)//2
        if lis[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lis[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
lis=[5,8,9,10,11]#in sorted order
n=9
if search(lis,n):
    print('found at',pos+1)
else:
    print('not found')
