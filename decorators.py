# A decorator is essentially a function that takes another function as an argument, 
# and returns a new function that adds some kind of functionality to the original function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
