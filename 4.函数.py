#调用函数
abs(1)


#数据类型转换
int('123')
float('123.12')

#定义函数 def
def ww_test(x):
    if x>=0:
        return x
    else:
        return -x
print(ww_test(-10))    

#空函数

#返回多个值

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#默认参数
def power(x, n=2):
    s=1
    while n>0:
        n = n -1
        s = s*x
    return s
print(power(5))

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
print(calc(1,2))

#关键字参数 参数扩展
def person(name,age,**kw):
     print('name:', name, 'age:', age, 'other:', kw)
person('ww',30) 
person('ww',30,gender='M', job='Engineer' )      

#命名关键字
def person(name,age,*,city,job):
    print(name,age,city,job)
person('ww',21, city = 'bb',job = 'aa')    