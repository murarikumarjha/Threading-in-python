import multiprocessing
def producer(q):
    for i in ['suda','kumar','ayan','raj']:
        q.put(i)

def consume(q):
    while True :
        item = q.get()
        if  item is  None :
            break 
        print(item)
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    m1 = multiprocessing.Process(target = producer , args =(queue,))
    m2 = multiprocessing.Process(target = consume , args =(queue,))
    m1.start()
    m2.start()
    queue.put('sudh')
    m1.join()
    m2.join()