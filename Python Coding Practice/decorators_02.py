
def decorator_func(fun):
    print("This is initial print statement /n")

    fun()

    print("After execution of decorator/modified function")

def modified_fun():
    print("I am New here")


decorator_func(modified_fun)

