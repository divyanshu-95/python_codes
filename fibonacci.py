howmany=int(input('how many terms : '))
num1,num2=0,1
count=0
if howmany<=0:
    print('Enter +ve number')
elif howmany==1:
    print(num1)
else:
    while count<howmany:
        print(num1)
        num3=num1+num2
        num1=num2
        num2=num3
        count+=1
    
