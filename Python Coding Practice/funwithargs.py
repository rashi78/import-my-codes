#args and kwargs

def funwithargs(*vars, **kvars):
    print(vars, kvars)

    for key, value in kvars.items():
        print(key, value)


funwithargs(1, 1, 2, k=123, l=12)
