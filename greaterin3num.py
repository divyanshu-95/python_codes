x=int(input('Enter first number : '))
y=int(input('Enter second number : '))
z=int(input('Enter third number : '))
if(x>y) and (x>z):
    print('first number is greater')
elif(y>x) and (y>z):
    print('second number is greater')
else:
    print('third number is greater')
