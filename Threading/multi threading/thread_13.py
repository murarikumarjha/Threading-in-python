# Thread Identifiers:- Native-id and ident 
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

print("identifier",t1.ident)
print("native identifier of t1 ",t1.native_id)

