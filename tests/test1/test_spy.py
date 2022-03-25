import unittest
from src.test1.spy import *


@Spy
def first(x):
    return x


@Spy
def second(x, y):
    return max(x, y)


print_usage_statistic(first)
