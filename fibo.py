def f(n):
    a,b=0,1
    if n==1:
        print(a)
    elif n<0:
        print('ntr +ve n')
    else:
        print(a,end=' ')
        print(b,end=' ')
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
n=int(input('ntr series: '))
f(n)
