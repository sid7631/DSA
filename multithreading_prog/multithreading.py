import threading
import os

def print_square(num):
    """
    function to print square of given num
    """
    task_info('print_square')
    print("Square: {}".format(num * num))

def print_cube(num):
    """
    function to print cube of given num
    """
    task_info('print_cube')
    print("Cube: {}".format(num * num * num))

def task_info(task_name):
    print("{} assigned to thread: {}".format(task_name,threading.current_thread().name))
    print("ID of process runiing {}: {}".format(task_name,os.getpid()))


if __name__ == "__main__":

    print("ID of process running main program: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")