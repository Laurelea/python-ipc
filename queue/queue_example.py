from multiprocessing import Process, Queue
import time
q = Queue()
def fun(name):
    time.sleep(1)
    q.put("hello" + str(name))
jobs = []
for i in range(10):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
while not q.empty():
    print(q.get())