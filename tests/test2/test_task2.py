import pytest
from src.test2.task2 import quicksort
import random as rnd
import copy


def test_simple():
    numbers_right = [1, 2, 3, 4, 5, 6, 7, 8]
    numbers = copy.deepcopy(numbers_right)
    rnd.shuffle(numbers)
    numbers = quicksort(numbers)
    assert numbers == numbers_right


def test_more_numbers():
    numbers_right = [x for x in range(99)]
    numbers = copy.deepcopy(numbers_right)
    rnd.shuffle(numbers)
    numbers = quicksort(numbers)
    assert numbers == numbers_right
