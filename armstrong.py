n=int(input())
#sum=0
def arm(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+(rem*rem*rem)
        n=n//10
    return sum
if n==arm(n):
        print('yes')
else:
        print('no')
