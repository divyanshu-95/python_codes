print('******WELCOME TO ATM******')
restart=('Y')
chances=3
balance=10000
while(chances>=0):
    pin=int(input('Enter your PIN : '))
    if pin==0000:
        print('u r in!')
        print('Balance 1')
        print('Withdraw 2')
        print('exit 3\n')
        while restart not in ('n','N','No','no','NO'):
            print('Balance 1')
            print('Withdraw 2')
            print('exit 3\n')
            opt=int(input('ntr choice : '))
            if opt ==1:
                print('Account Balance is Rs. ',balance)
                if restart in ('n','N','No','no','NO'):
                    print('Done')
                    break
            elif opt==2:
                withdraw=float(input('How much u want ? 100,500,2000 for other press 1 :'))
                if withdraw in [100,500,2000]:
                    balance=balance-withdraw
                    print('\nYour remaining balance Rs. : ',balance)
                    restart=input('Would you like to go back ? ')
                    if restart in ('n','N','No','no','NO'):
                        print('Thanks')
                        break
                elif withdraw!=[100,500,2000]:
                        print('Enter valid amount \n')
                        restart=('Y')
                elif withdraw==1:
                        withdraw=float(input('ntr desired amt : '))
            elif opt==3:
                print('thnx for coming ur card is returning')
                restart=('Y')
    
    elif pin!=('0000'):
        print('incorrect pin')
        chances=chances-1
        if chances==0:
            print('\nNo more tries')
            break
        
