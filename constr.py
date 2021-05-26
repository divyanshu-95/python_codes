class comp:
    def __init__(self):
        self.name='srk'
        self.age=20
    def update(self):
        self.age=30#use of self is to use change value according to which are currently
                    #working upon
c1=comp()
c2=comp()
#we can change the values also after initialization like here

c1.name='sssrrrkkk'
c1.age=19

print(c1.name)
print(c2.name)
