def curry_explicit(func, arity):
    """Returns curried function"""
    if arity < 0:
        raise RuntimeError("Arity should be positive")
    if arity < 2:
        return func

    def curry(arg):
        def simplify(*args):
            if len(args) != arity - 1:
                raise RuntimeError("Curry: Arity doesn't match with the number of args")
            return func(arg, *args)

        return curry_explicit(simplify, arity - 1)

    return curry


def uncurry_explicit(func, arity):
    """Returns function with the number of args defined in arity"""
    if arity < 0:
        raise RuntimeError("Arity should be positive")

    def uncurry(*args):
        if len(args) != arity:
            raise RuntimeError("Uncurry: Arity doesn't match with the number of args")
        ctor = curry
        for arg in args:
            ctor = ctor(args)
        return ctor

    return uncurry
