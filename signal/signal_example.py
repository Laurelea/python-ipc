import signal
import os

def handler(signum, frame):
    print('Обработчик сигнала вызывается с помощью signal', signum)
    raise OSError("Не удалось открыть устройство!")

# Устанавливает обработчик сигнала и 5-секундный сигнал тревоги
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# Tего open() может зависать бесконечно
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Отключает сигнализацию