class computer:
    def __init__(self,cpu,ram):#init called automatically
        #print('in init')
        self.cpu=cpu
        self.ram=ram
    def config(self):
        #self is the obj which is passing
        print(self.cpu,self.ram)

com1=computer('i5',16)#obj creation
com2=computer('i3',16)
#computer.config(com1)

com1.config()
com2.config()
#special method->__init__
