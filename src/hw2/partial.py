def curry_explicit(func, arity):
    if arity < 0:
        raise TypeError("Arity should be positive")
    if arity < 2:
        return func
    def curry(arg):
        def simplify(*args):
            if len(args) != arity - 1:
                raise TypeError("Curry: Arity doesn't match with the number of args")
            return (arg, *args)
        return curry_explicit(simplify, arity-1)
    return curry


def uncurry_explicit(func, arity):
    if arity < 0:
        raise TypeError("Arity should be positive")
    def uncurry(*args):
        if len(args) != arity:
            raise TypeError("Uncurry: Arity doesn't match with the number of args")
        for arg in args:
            ctor = ctor(args)
        return ctor
    return uncurry
