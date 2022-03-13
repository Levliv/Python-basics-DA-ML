from threading import Thread
from src.hw3.semaphore import *


def create_string(dictionary, key, value):
    with dictionary.modify_safely as dictionary:
        dictionary[key] = value


def test_multi_threading():
    first_dict = ConcurrentDict()
    threads = [Thread(target=create_string, args=(first_dict, f"key:{number}", number)) for number in range(30)]
    for thread in threads:
        thread.Start()
    for thread in threads:
        thread.Join()

    for number in range(30):
        assert first_dict[f"key_{number}"] == number
