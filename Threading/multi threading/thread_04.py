# Thread for methods
from threading import Thread

class Example :

    @staticmethod
    def display(n):
        for i in range(n):
            print('static method in Thread')

e1 = Example()
t1 = Thread(target = Example.display, args =(2,) )
t1.start()

for i in range(3):
    print("welcome!")

