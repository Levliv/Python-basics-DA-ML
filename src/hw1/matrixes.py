from src.hw1.vectors import vector_multiplication


def matrix_size_check(first_matrix, second_matrix):
    sizes1 = list(map(len, first_matrix))
    sizes2 = list(map(len, second_matrix))
    if sizes1 != sizes2:
        raise RuntimeError("Matrices should have same sizes for operations")


def matrix_transpose(matrix):
    return tuple(zip(*matrix))


def matrix_sum(first_matrix, second_matrix):
    matrix_size_check(first_matrix, second_matrix)
    return tuple(tuple(map(sum, zip(x, y))) for (x, y) in (zip(first_matrix, second_matrix)))


def matrix_multiplication(first_matrix, second_matrix):
    second_matrix_transposed = matrix_transpose(second_matrix)
    matrix_size_check(first_matrix, second_matrix_transposed)
    return matrix_transpose(
        tuple(tuple(vector_multiplication(x, y) for x in first_matrix) for y in second_matrix_transposed)
    )
