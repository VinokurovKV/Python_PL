class Tester:
    def __init__(self, fun):
        self.fun = fun
    def __call__(self, suite, allowed=()):
        result = 0
        for tuples in suite:
            try:
                self.fun(*tuples)
            except Exception as exception:
                if allowed and isinstance(exception, tuple(allowed)):
                    result = -1
                else:
                    return 1
        return result
