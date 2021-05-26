#exce
a=5
b=0
try:
    print(a/b)
except Exception as e:
    print('err',e)
finally:
    print('closed')
