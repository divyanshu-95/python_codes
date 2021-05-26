#scope
a=10
def some():
    a=9
    x=globals()['a']
    
    print(a)
print(a)#outer is global variable ,it is
#possible that two variable exist in code but scope is different
#in function is local variable
#we can use global vaiable in the function accessable
#if we want give global var in func than syntax :: global a 
some()
