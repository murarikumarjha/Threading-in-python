from threading import Thread, current_thread
def display():
    print('Hello world')

def show():
    for i in range(3):
        print('welcome')
    
t1 = Thread(target = display)
t2 = Thread(target = show)

t1.name = "shantanu"
print(t2.getName())

current_thread().name = 'jay'
print(current_thread().name)