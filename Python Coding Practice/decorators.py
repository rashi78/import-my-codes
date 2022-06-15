def decfun(fun):
    def wrapper():
        print("Hii")
        fun()
        print('Bye')
    return wrapper


@decfun
def mainfun():
    print('Hello')

mainfun()
