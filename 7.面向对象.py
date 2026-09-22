#
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板

class Student(object):
    pass

# 创建类的实例
bar = Student()

bar.name = 'Arcan'


#特殊方法__init__前后分别有两个下划线！！！
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score= score
    pass

bar = Student('simon',100)

#数据封装
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bar = Student('simon',100)        
bar.print_score()

#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

#访问限制
#前面加2个下划线，变成私有变量，只有内部访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

#外部如果要获取
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


#多态
# 
class Animal(object):
    def run(self):
        print('Animal is running...')

def run_twice(animal):
    animal.run()
    animal.run()

class Dog(Animal):
   def run(self):
        print('Dog is running...')

class Cat(Animal):
   def run(self):
        print('Cat is running...')
        
run_twice(Dog())
run_twice(Cat())

#静态语言和动态语言

#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class People(object):
   def run(self):
        print('People is running...')

run_twice(People())


        