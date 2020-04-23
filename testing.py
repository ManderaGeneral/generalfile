"""
Random testing
"""
import unittest
import multiprocessing as mp

from generalfile import *

import time
import datetime as dt




def threadTestWrite(queue, i):
    queue.put("write {}".format(File.write("test.txt", i, overwrite=True)))

def threadTestRead(queue):
    queue.put("read {}".format(File.read("test.txt")))


# def t1():
#     with open("test.txt", "x") as textIO:
#         textIO.write("hello")
#         time.sleep(3)
#
# def t2():
#     time.sleep(1)
#     with open("test.txt", "r") as textIO:
#         print(textIO.read())


if __name__ == '__main__':
    File.setWorkingDir("test/tests")

    # mp.Process(target=t1).start()
    # mp.Process(target=t1).start()

    threads = []
    queue = mp.Queue()
    for i in range(count := 10):
        threads.append(mp.Process(target=threadTestWrite, args=(queue, i)))
        threads.append(mp.Process(target=threadTestRead, args=(queue,)))
    for thread in threads:
        thread.start()


    results = []
    for i in range(count*2):
        results.append(queue.get())
    print(results)


