num=int(input('enter no. : '))
i=0
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print('not prime')
            break
    else:
            print('prime')
            
else:
    print('not prime')
