from math import sqrt, acos
from typing import List

Vector = List[Union[int, float, complex]]


def vector_multiplication(first_vector: Vector, second_vector: Vector):
    if len(first_vector) != len(second_vector):
        raise AssertionError("For multiplications vectors should have the same sizes")
    try:
        return sum(map(lambda x: x[0] * x[1], list(zip(first_vector, second_vector))))
    except (TypeError, KeyError):
        raise AssertionError("Can't perform an operation on these vectors")


def vector_norm(vector: Vector):
    return sqrt(sum(x * x for x in vector))


def vector_angle(first_vector: Vector, second_vector: Vector):
    try:
        return acos(
            vector_multiplication(first_vector, second_vector)
            / (vector_norm(first_vector) * vector_norm(second_vector))
        )
    except ZeroDivisionError:
        raise AssertionError("At least one of the vectors must not be zero")
