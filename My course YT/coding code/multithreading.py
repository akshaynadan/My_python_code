import threading
import time  


def eat():
    time.sleep(3)
    print("im eating")
def drink():
    time.sleep(4)
    print("im drinking")
    
def sleep():
    time.sleep(5)
    print("im sleeping")


x = threading.Thread(target=eat)
x.start()

y = threading.Thread(target=drink)
y.start()

z = threading.Thread(target=sleep)
z.start()

x.join()
y.join()
z.join()

# eat()
# drink()
# sleep()




print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
