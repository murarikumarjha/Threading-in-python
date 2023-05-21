# 1) Create a Thread without using an Explicit function:

# Import required modules
from threading import *	


# Explicit function
def display() :				
    for i in range(10) :
	    print("Child Thread")


# Driver Code	
	
# Create object of thread class	
Thread_obj = Thread(target=display)		

# Executing child thread
Thread_obj.start()			

# Executing main thread
for i in range(10):			
    print('Main Thread')
