def person(name, **data):#** use for pass multiple args help of variabkes
    print('name' ,name)
    #print(data)
    for i,j in data.items():
        print(i,j)
person(name='sr',age=18,city='mum',mob=1234567890)
