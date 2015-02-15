from threading import Thread
from datetime import datetime

COUNT = 1000000000

def get_max(lst):
    for _ in lst:
        pass


def thread_test():
    t1 = Thread(None, get_max, "t1", (xrange(COUNT),))
    t2 = Thread(None, get_max, "t2", (xrange(COUNT),))
    start = datetime.now()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print "With 2 thread:", datetime.now() - start

def flat_test():
    start = datetime.now()
    get_max(xrange(COUNT))
    get_max(xrange(COUNT))
    print "With one thread:", datetime.now() - start

if __name__ == "__main__":
    flat_test()
    thread_test()