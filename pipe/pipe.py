from multiprocessing import Process, Pipe
import os, time

# Создать объект конвейера
# Если параметр равен False, дочерний элемент может только получать, а родитель может только отправлять
# child_conn, parent_conn = Pipe(False)
child_conn, parent_conn = Pipe()


# Subprocess function
def fun(name):
    time.sleep(1)
    # Отправляем строку в трубу
    child_conn.send('hello' + str(name))
    print(os.getppid(), "----", os.getpid())
    time.sleep(1)

jobs = []
# Создайте 5 дочерних процессов
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()
for i in range(5):
    data = parent_conn.recv()
    print(f'data received from parent: {data}')
    time.sleep(1)
for i in jobs:
    i.join()
