def greet():
    print('hello')
greet()#explicitly call

def add(x,y):
    c=x+y
    print(c)
add(4,5)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)
