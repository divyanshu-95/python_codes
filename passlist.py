def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list=[20,21,22,55,85,36,56,96]

even,odd=count(list)
#print('even',even)
#print('odd',odd)
print('even : {} and odd : {}'.format(even,odd))
