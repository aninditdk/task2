def outer(a,b):
    def inner():
        c=a+b
        return c
    return inner()+5
a,b=int(input()),int(input())
d=outer(a,b)
print(d)


