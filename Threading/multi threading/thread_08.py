# creating and using temp / temperary variable 
# constructor
from time import sleep
from threading import Thread
video = ['oop syallbus','constructor ','distructor','file handling']
# checking construction and calling constrction
class Myclass(Thread):
    def __init__(self,val):
        print('constructor called')
        self.kid = val
        Thread.__init__(self)
        
    def construction_call(self):
        print('construction is called ')
    def run(self):
        a = 10
        b = 20
        self.construction_call()
        if self.kid:
            print("suitable for kids")
        for vid in video:
            print(f"{vid} started uploding...")
            sleep(1)
            print(f'{vid} uploaded.')
        self.temp = a+b

t1 = Myclass(True)
t1.start()
sleep(10)
print("temp var is ", t1.temp)
