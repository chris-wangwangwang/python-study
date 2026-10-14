#读文件

f = open(r"C:\Users\11329\Desktop\docker.txt", 'r')
print(f.read())
f.close()

#添加异常
try:
    f = open(r"C:\Users\11329\Desktop\docker.txt", 'r') 
    print(f.read())
finally:
    if f:
        f.close()    

#with 自动调用close
with open('/path/to/file', 'r') as f:
    print(f.read())    

#二进制
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open(r"C:\Users\11329\Desktop\docker.jpg", 'rb')

#字符编码
with open(r"C:\Users\11329\Desktop\docker.txt", 'r', encoding='gbk') as f:
    print(f.read())    


#写文件 w
f = open(r"C:\Users\11329\Desktop\docker.txt", 'w')  

with open(r"C:\Users\11329\Desktop\docker.txt", 'w') as f:
    print(f.write('hello world'))   

#操作文件
# os     

#序列化
#变量从内存中变成可存储或传输的过程称之为序列化
#pickle
import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)