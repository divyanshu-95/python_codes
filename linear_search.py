pos=-1

def search(lis,n):
    i=0
    while i<len(lis):
        if lis[i]==n:
            globals()['pos']=i#bcz for local var
            return True;
        i+=1
    return False;
lis=[5,8,4,6,9,12]
n=9
if search(lis,n):
    print('found at',pos)
else:
    print('not found')
