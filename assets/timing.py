import threading
import time


class SetInterval:
    def __init__(self):
        self.__running = True

    def run(self, seconds, callback):
        while self.__running:
            time.sleep(seconds)
            lock = threading.Lock()
            lock.acquire()
            callback()
            lock.release()
            print(threading.active_count())

    def terminate(self):
        self.__running = False

    def call(self, func, seconds: int = 1):
        self.__running = True
        threading.Thread(target=self.run, args=(seconds, func)).start()
