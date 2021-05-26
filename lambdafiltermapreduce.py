#def is_even(n):
 #   return n%2==0
from functools import reduce
nums=[3,2,5,6,8,9,4,7]
evens=list(filter(lambda n : n%2==0,nums))#filter func take value
#(filter take two args fun and iterable)

#use map
doubles=list(map(lambda n:n*2,evens))
#use reduce
sum=reduce(lambda a,b : a+b,doubles)
print(sum)
