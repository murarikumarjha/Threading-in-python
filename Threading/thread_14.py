# Thread Identifiers:-other id = getpid()
import os
from threading import Thread
def display():
    for i in range(4):
        print("welcome!")
def show():
    for i in range(3):
        print("Hello world")

t1 = Thread(target= display)
t2 = Thread(target = show)

t1.start()
t2.start()

print("get pid id are",os.getpid())

