#字符串转义
# I'm "OK"!  \"
print("I'm \"OK\"")

#运算符
print(3>2)

#空值 None

#变量
#动态语言
#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a= 123
a='abc'

#变量的定义
#a = 'ABC'
#Python解释器干了两件事情： 
# 1.在内存中创建了一个'ABC'的字符串；
# 2.在内存中创建了一个名为a的变量，并把它指向'ABC'。
#a = 'ABC'
#b = a
#a = 'XYZ'
#print(b)
#流程：
# 1.执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
# 2.执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：
# 3.执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：


#常量  通常用全部大写的变量名表示常量


#字符串
#编码格式
#ASCII，Unicode， UTF-8 编码的区别
#计算机内存中的编码都是用的Unicode编码，保存硬盘和传输用UTF-8
# 'ABC'.encode('ascii')
# '中文'.encode('utf-8')

#填充

print(len('123'))
print('%2d-%02d' % (3,1))
print('%.2f' % 3.14556)

#format()
print("'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)")
#f-string
#print(f'The area of a circle with radius {r} is {s:.2f}')
a1 = 72
a2 = 85
a3 = (a2-a1)/a1
print("小明提升了 %.1f%%" % a3)

#list
#list是一种有序的集合，可以随时添加和删除其中的元素。元素可以不同
# append
c1 = ['Michael', 'Bob', 'Tracy']
a= c1[-1] #最后一个
c1.insert('123')
c1.pop(1) #删除下标

#tuple 元组 tuple不可变
c1 = ['Michael', 'Bob', 'Tracy']
#c1这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
#定义元组
t = (1,2)
t = (1,) #一个要用，
t = ()