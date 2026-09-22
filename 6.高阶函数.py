#函数也是变量
def add(x, y, f):
    return f(x) + f(y)

x = -5
y = 6
f = abs