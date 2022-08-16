import multiprocessing
import os

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return n*n

if __name__ == '__main__':

    mylist = [1,2,3,4,5,6,7,8,9,10]

    p = multiprocessing.Pool()

    result = p.map(square, mylist)

    print(result)