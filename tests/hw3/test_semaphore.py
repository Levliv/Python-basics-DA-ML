from threading import Thread
from src.hw3.semaphore import ConcurrentDict


def create_string(dictionary: dict, key: str, value: int):
    with dictionary.modify_safely as dictionary:
        dictionary[key] = value


def test_multi_threading():
    first_dict = ConcurrentDict()
    threads = [Thread(target=create_string, args=(first_dict, f"key_{number}", number)) for number in range(1, 5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    with first_dict.modify_safely() as d:
        for number in range(1, 5):
            assert d[f"key_{number}"] == number
