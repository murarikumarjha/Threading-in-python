# change the name of thread from Thread-1 to 'shantanu'

from threading import Thread
def display():
    print('Hello world')

def show():
    for i in range(3):
        print('welcome')
    
t1 = Thread(target = display)
t2 = Thread(target = show)

t1.name = "shantanu"
print(t2.getName())
print(t1.name)