nums=[12,13,18,21,26]#20,25 div by 5
for num in nums:
    if num %5==0:
        print(num)
        #print only first number in list which is divisible by 5
        break#this is for above cond(it is compulsory)
else:# for not condi
        print('not found')
