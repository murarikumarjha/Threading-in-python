from threading import Thread,main_thread,active_count,enumerate,get_native_id
def display():
    print("native id of t1 thread: ",get_native_id())
    print('main thread details', main_thread())
    for i in range(4):
        print("Hello world")
    def show():
        for i in range(3):
            print('Hii')
    show()
        
t1 = Thread(target=display)
print("before",t1.is_alive())
t1.start()
print("native id of main thread: ",get_native_id())
print("number of active count: ",active_count())
print("list of running threads are : ",enumerate())

print("after",t1.is_alive())