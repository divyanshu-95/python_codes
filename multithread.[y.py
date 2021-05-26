#every execution have 1 thread main thread
from time import sleep
from threading import * 
class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(i)
class hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(i)
t1=hello()
t2=hi()

t1.start()
sleep(0.2)#for not collision
t2.start()
t1.join()
t2.join()#for not collision to main thread
#3threads(t1,t2,sleep)
print('bi')#responsible is main thraed
