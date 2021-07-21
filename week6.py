def f(*args, **kwargs):
   print(args, kwargs)
a = [1, 2]
d = {'x': 3, 'y': 4}
# f(a)
# f(*a)
# f(**a)
# f(d)
# f(*d)
# f(**d)
# f(a, d)
# f(*a, d)
# f(a, **d)
f(*a, **d)