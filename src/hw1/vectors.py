from math import sqrt, acos


def check_vector(vector):
    if not ((type(vector) == list) | (type(vector) == tuple)):
        return (False, "Data should be stored in tuple of vector")
    for x in vector:
       if not ((type(x) == int) | (type(x) == float) | (type(x) == complex)):
           return (False, "Vectors should consist of int, float of complex values")
    return (True, "Ok")

def check_multivector(*args):
    for vector in args:
        check_result, error_message = check_vector(vector)
        if not check_result:
            return (False, error_message)
    return (True, "OK")

def vector_check_exception_raiser(*args):
    map(lambda x: check_vector(x), args)
    (check_result, error_message) = check_multivector(*args)
    if not check_result:
        raise RuntimeError(error_message)

def vector_multiplication(first_vector, second_vector):
    vector_check_exception_raiser(first_vector, second_vector)
    return sum(map(lambda x: x[0] * x[1], list(zip(first_vector, second_vector))))

def vector_norm(vector):
    vector_check_exception_raiser(vector)
    return sqrt(sum(x*x for x in vector))

def vector_angle(first_vector, second_vector):
    vector_check_exception_raiser(first_vector, second_vector)
    return acos(vector_multiplication(first_vector, second_vector)/(vector_norm(first_vector) * vector_norm(second_vector)))

