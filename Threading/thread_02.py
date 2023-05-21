# #2) Create Thread by extending Thread Class : 
from threading import *

# extending thread class
class Mythread(Thread):

    # Target functon for thread
    def run(self):
        for i in range(5):
            print("child thread")

# driver code 

# creating thread  class object 
t = Mythread()
# Executing of target fucntion
t.start()
# Exception of main thread
for i in range(3):
    print("main thread")