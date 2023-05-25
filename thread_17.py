# neeed of join method
'''              if a thread wants to wait for some other thead, then we should go for join() method.
'''
from threading import Thread
from time import sleep

def upload():
    print("uploding starts")
    sleep(3)
    print("video uploaded")

def notification():
    print("sending notification to subscribers code ")

t1  = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()
# Main thread code
for i in range(4):
    print("Hello")