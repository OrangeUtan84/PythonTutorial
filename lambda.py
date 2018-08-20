def make_inc():
    return lambda x: x + 1





f = lambda a, b: a + b

print(f(1,2))



increment = make_inc()

print(increment(5))