class FooError(Exception): pass

def foo():
    raise FooError()

try:
    foo()
except FooError as e:
    #raise e
    #raise Exception()
    raise Exception from e
finally:
    print("FINALLY")
