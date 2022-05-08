import random
import copy
from multiprocessing import Process
from multiprocessing import Pipe
from typing import List


def quicksort_pipe(numbers: List[int], conn, proc_number):
    if len(numbers) <= 1:
        conn.send(numbers)
        conn.close()
        return
    p = numbers.pop(random.randint(0, len(numbers) - 1))
    left = [x for x in numbers if x < p]
    pconn_left, cconn_left = Pipe()
    left_process = Process(target=quicksort_pipe, args=(left, cconn_left, proc_number - 1))
    right = [x for x in numbers if x >= p]
    pconn_right, cconn_right = Pipe()
    right_process = Process(target=quicksort_pipe, args=(right, cconn_right, proc_number - 1))
    left_process.start()
    right_process.start()
    conn.send(pconn_left.recv() + [p] + pconn_right.recv())
    conn.close()
    leftProc.join()
    rightProc.join()


def quicksort(numbers):
    nums = copy.deepcopy(numbers)
    pconnection, cconnection = Pipe()
    process = Process(target=quicksort_pipe, args=(nums, cconnection, 3))
    process.start()
    nums = pconnection.recv()
    process.join()
    return nums
