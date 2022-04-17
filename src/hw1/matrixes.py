from vectors import vector_multiplication, vector_check_exception_raiser


def matrix_size_check(first_matrix, second_matrix):
    sizes1 = list(map(len, first_matrix))
    sizes2 = list(map(len, second_matrix))
    if sizes1 != sizes2:
        raise RuntimeError("Martixes should have same sizes for addition")


def matrix_transpose(matrix):
    return list(zip(*matrix))


def matrix_sum(first_matrix, second_matrix):
    martix_size_check(first_matrix, second_matrix)
    vector_check_exception_raiser(*first_matrix, *second_matrix)
    return [list(map(sum, zip(x, y))) for (x, y) in (list(zip(first_matrix, second_matrix)))]


def matrix_multiplication(first_matrix, second_matrix):
    second_matrix_transposed = matrix_transpose(second_matrix)
    martix_size_check(first_matrix, second_matrix_transposed)
    vector_check_exception_raiser(*first_matrix, *second_matrix)
    return matrix_transpose([list(vector_multiplication(x, y) for x in first_matrix) for y in second_matrix_transposed])


if __name__ == "__main__":
    print(matrix_transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(matrix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(matrix_multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
