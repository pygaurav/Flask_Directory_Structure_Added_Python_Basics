from app import security
import datetime
import functools

class AnotherStudent(security.Student):
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)

    def getTimeofTicket(self):
        self.time = datetime.datetime.now()
        print(self.time)


def my_custom_decorator(func):
    @functools.wraps(func)
    def f(*args,**kwargs):
        print(sum(args))
        print("Name is "+kwargs['name'])
        print("Inside the func")
        func(*args,**kwargs)
        print("Outside the func")
    return f

@my_custom_decorator
def hello(a,b,name):
    print("Executing the func")


def my_custom_decorator_redefined(val):
    def myfunc(func):
        @functools.wraps(func)
        def f():
            print("Inside the main loop")
            func()
            print("Outside the main loop")
        return f
    return myfunc

@my_custom_decorator_redefined(58)
def hellyeah():
    print("Hello World")

