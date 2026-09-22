#条件判断
age  = 18
if age>17:
    print("you")

# match case
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


#循环        
for x in [1,2,3,4,5,6,7,8,9]:
    print(x)



#字典 dict 类似map 使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# set  也是一组key的集合，但不存储value。由于key不能重复，
s = {1, 2, 3}
s.add(4)
s.remove(4)