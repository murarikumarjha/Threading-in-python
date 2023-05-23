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
        self.construction_call()
        if self.kid:
            print("suitable for kids")
        for vid in video:
            print(f"{vid} started uploding...")
            sleep(3)
            print(f'{vid} uploaded.')

t1 = Myclass(True)
t1.start()

for i in range(4):
    sleep(0.5)
    print("checking copyright")