from multiprocessing import Process, Queue, current_process
import time
import queue


def do_job(tasks_active, tasks_completed):
    while True:
        try:
            '''
                пытаемся получить задачу из очереди. `get_nowait()` 
                выбросит исключение queue.Empty, если очередь будет пуста.
            '''
            task = tasks_active.get_nowait()
        except queue.Empty:
            break
        else:
            '''
                если исключения не было, отправляем сообщение в очередь завершенных задач
            '''
            print(task)
            tasks_completed.put(task + ' выполнена процессом ' + current_process().name)
            time.sleep(.5)  # если закомментировать эту строку все такси будут выполнены одним процессом - первым


if __name__ == '__main__':
    number_of_task = 10
    number_of_processes = 4
    tasks = Queue()
    tasks_done = Queue()
    processes = []

    for i in range(number_of_task):
        tasks.put("Задача № " + str(i))

    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks, tasks_done))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not tasks_done.empty():
        print(tasks_done.get())