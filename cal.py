def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print('what u want : ')
print('1.Add  ')
print('2.Substract : ')
print('3.Multiply : ')
print('4.Divide : ')

while True:
    choice=input('Enter choice(1/2/3/4): ')
    if choice in ('1','2','3','4'):
        a=float(input('Enter 1st number : '))
        b=float(input('Enter 2nd number : '))
        if choice =='1':
            print(add(a,b))
        elif choice=='2':
            print(sub(a,b))
        elif choice=='3':
            print(mul(a,b))
        elif choice=='4':
            print(div(a,b))
    else:
        print('Invalid Input...')    

