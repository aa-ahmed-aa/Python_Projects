import threading

class message(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x1 = message(name = 'send message')
x2 = message(name='recieve message')
x1.start()
x2.start()