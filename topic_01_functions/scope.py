x = 1
def foo(y):
    x = 2
    print('x=', x)
    return y + 1
print('x=', x)
print('foo(x)=', foo(x))
print('x=', x)
