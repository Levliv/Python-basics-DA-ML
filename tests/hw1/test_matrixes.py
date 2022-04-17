import pytest
from src.hw1.matrixes import matrix_transpose, matrix_sum, matrix_multiplication


def test_matrix_transpose():
    assert matrix_transpose(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == ((1, 4, 7), (2, 5, 8), (3, 6, 9))


def test_matrix_sum():
    sum = matrix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert sum == ((2, 4, 6), (8, 10, 12), (14, 16, 18))


def test_matrix_multiplication():
    mul = matrix_multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[4, 23, 2], [12, 53, 64], [12, 83, 5]])
    assert mul == ((64, 378, 145), (148, 855, 358), (232, 1332, 571))
