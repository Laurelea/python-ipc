signal(SIGCHLD, SIG_IGN)
from signal_example_01 import *
import os, time


# Функция обработки сигналов с фиксированным форматом параметров
def handler(sig, frame):
    if sig == SIGALRM:
        print("Полученный тактовый сигнал")
    elif sig == SIGINT:
        print("SIGINE не закончится после получения")


alarm(7)

# Обработка сигнала через функцию
signal(SIGALRM, handler)
signal(SIGINT, handler)

while True:
    print("waiting for signal")
    time.sleep(2)