import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power, lock):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0
        self.lock = lock

    def run(self):
        with self.lock:
            print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power


            if self.enemies < 0:
                self.enemies = 0

            with self.lock:
                print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        with self.lock:
            print(f"{self.name} одержал победу спустя {self.days} дня(дней)!")



if __name__ == "__main__":
    lock = threading.Lock()
    knight1 = Knight("Рыцарь Артур", 10, lock)
    knight2 = Knight("Рыцарь Ланселот", 20, lock)

    knight1.start()
    knight2.start()

    knight1.join()
    knight2.join()
