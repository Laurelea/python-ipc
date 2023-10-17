from multiprocessing import Process, Pipe

def processor(conn):
    for i in range(5):
        conn.send([i, 'Привет', None, 256])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=processor, args=(child_conn,))
    p.start()
    while True:
        res = parent_conn.recv()
        print(res)# распечатает "['Привет', None, 256]"
    p.join() #  процесс не завершится, так как при пустом конвейере соединение будет вечно в ожидании
