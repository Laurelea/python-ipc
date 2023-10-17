'''Один процесс пишет в очередь сообщение ping, а другой — вычитывает сообщение из очереди и печатает его в консоль.
Каждому процессу отдаётся один и тот же объект queue, через который процессы могут взаимодействовать друг с другом и
при этом не быть связанными.'''

from multiprocessing import Process, Queue
from time import sleep

def produce(queue: Queue):
    while True:
        message = 'ping'
        queue.put(message)
        sleep(1)

def consume(queue: Queue):
    # оператор := ("морж") используется для присвоения переменной во время вычисления другого выражения
    while message := queue.get():
        print(message)

if __name__ == '__main__':
    queue = Queue()
    producer = Process(target=produce, args=(queue,))
    consumer = Process(target=consume, args=(queue,))
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
