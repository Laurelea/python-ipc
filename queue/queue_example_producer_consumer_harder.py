from multiprocessing import Process, Queue
import random
import time

"""
Задача производитель–потребитель описывает два процесса: одна сторона выступает производителем, а другая — потребителем. 
Они совместно используют общий буфер фиксированного размера. Основная задача производителя состоит в добавлении данных в буфер. 
В это же время, потребитель использует данные из буфера и удаляет их. Производитель никогда не переполнит буфер сверх нормы, 
а потребитель будет ждать данные, если буфер пуст.
Реализация задачи состоит в том, что производитель приостанавливает своё выполнение, когда буфер заполнен. 
Как только потребитель использует элемент полного буфера, то производитель проснётся и начнёт снова наполнять его данными. 
Аналогично потребитель приостанавливает выполнение, когда буфер пуст. Как только производитель наполнит его новыми данными, 
потребитель продолжит работу.
Это решение может быть реализовано стратегиями взаимодействия между процессами, совместной памятью или обменом сообщениями. 
Но неверное решение может приводить к взаимной блокировке (deadlock), при которой оба процесса ожидают пробуждения.
"""


class Producer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for idx in range(5):
            item = random.randint(0, 100)
            self.queue.put(item)
            print(f'{idx} Producer: запись {item} добавлена {self.name}\n')
            time.sleep(1)


class Consumer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print('Очередь пуста')
                break
            else:
                time.sleep(1)
                item = self.queue.get()
                print(f'Consumer: запись {item} получена из {self.name} \n')
                time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
