import pytest
from src.hw1.vectors import vector_norm, vector_angle, vector_multiplication
from math import sqrt, radians


def test_vector_norm():
    vector = [x for x in range(1, 5)]
    assert vector_norm(vector) - sqrt(30) < 0.0000001


def test_vector_multiplication():
    first_vector = (1, 2, 3)
    second_vector = (4, 5, 6)
    assert vector_multiplication(first_vector, second_vector) == 32


def test_vector_multiplication_2():
    first_vector = (0, 1)
    second_vector = [2, 0]
    assert vector_multiplication(first_vector, second_vector) == 0


def test_vector_angle():
    first_vector = (0, 1)
    second_vector = (2, 0)
    assert vector_angle(first_vector, second_vector) - radians(90) < 0.000001
