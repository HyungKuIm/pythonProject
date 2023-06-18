import threading
import time

def worker(msg):
    print("{} is start : {}".format(threading.currentThread().getName(), msg))
    time.sleep(5)
    print("{} is end".format(threading.currentThread().getName()))

def main():
    for i in range(10):
        msg = "hello {}".format(i)
        th = threading.Thread(target=worker, name="[th def {}]".format(i), args=(msg,))
        th.start()


if __name__ == "__main__":
    main()