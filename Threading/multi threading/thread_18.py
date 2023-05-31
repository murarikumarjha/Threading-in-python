from threading import Thread
import time
def square(num):
    print("Finding square...")
    time.sleep(1)
    print(f"square of {num} is: ",num**2)

def cube(num):
    print("Finding cube...")
    time.sleep(1)
    print(f"cube of {num} is:", num**3)
begin = time.time()
t1= Thread(target=square, args=(3,))
t2= Thread(target=cube, args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print('total time taken :',time.time()-begin)

# another program without using multithreading
def square_num(num):
    print("Finding square_num...")
    time.sleep(1)
    print(f"square of {num} is: ",num**2)

def cube_num(num):
    print("Finding cube_num...")
    time.sleep(1)
    print(f"cube of {num} is:", num**3)
begin_num = time.time()
square_num(3)
cube_num(3)
print("toal num time :",time.time()-begin_num)
#its take time