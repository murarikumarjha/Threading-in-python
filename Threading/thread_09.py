# get the name of Thread by getName() or by print(t1.name) fuction 

from threading import Thread
def display():
    print('Hello world')

def show():
    for i in range(3):
        print('welcome')
    
t1 = Thread(target = display)
t2 = Thread(target = show)

print(t1.getName())
print(t2.getName())