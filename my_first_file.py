# print('Hello Python')

# ' ' " " ''' ''' """ """

# a = 'I Love "Bangladesh"'
# a = '''Lorem Ipsum is simply dummy 
# text of the printing and typesetting i
# ndustry. Lorem Ipsum has been the industry's standard dummy text ever s
# ince the 1500s, when an unknown printer took a galley of type and scrambled it to make a type
#  specimen book. It has survived not only
#    five centuries, but also the leap into 
#  electronic typesettin
#  g, remaining essentially unchanged. It was popularised in the 1960s with the
#    release of Letraset sheets containing Lorem
#  Ipsum passages, and more recently with deskt
#  op publishing software like Aldus PageMaker in
#  cluding versions of Lorem Ipsum.'''



# print(a)
# '''This is my a varibale'''

# a = 'I Love'
# b = 'Bangladesh'
# c = a + " " + b
# print(c)

# a = 'I Love Bangladesh'

# print(len(a))

# print(a[-17:-11])

# print(a[0:50])
# print(a[-1])

# a = 'ei love'
# b = 'Bangladesh'

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.index('l'))
# print(a.count('l'))
# print(a.find('B'))
# print(a.replace('Bangladesh', 'India'))
# c = a.strip('e') +" " + b
# print(c)
# a = 'I Love  \'Bangladesh gghgjhgjhgjhgjhg'

# print(a.swapcase())
# print(a)

# print(len(a))


# b = 1971
# print(f'I Love {b} Bangladesh')
# print(a.format(b))

# a = input('Enter A Country : ')

# print(f'I Love {a}')
# print(a.upper())

# a = 'HelloRWT'
# print(a[::-1])

# a = 'hellow'
# print (a[::-2])
# OUtput = e
# print(a[-6:])

# Arithmetic Operator
# ======================

# + - * / % ** //

# a = 40

# b = 3

# print(b / a)

# a = 10
# print(a)
# a = a + 2
# a = 2

# print(a)

# == != > < >= <=

# a = 10

# b = 10

# print(not(a > 12 or b > 25) )
# print(a is not b)

# and or not

# a += 12

# a = a + 12

# print(a)

# a = 'i love bangladesh'

# print('b' not in a)

# & | ~ ^

# print( 6 | 3)
# 6 = 0110
# 3 = 0011
# ---------------------
# 0010
# 0111

# 0 = 0000
# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101
# 6= 0110
# 7 = 0111
# 8 = 1000
# 0 1

# 1 1 = 1
# 1 0 = 0
# 0 0 = 0
# 0 1 = 0

# print(bytes(1 & 1))

# a = 10

# b = 10

# print(a > b)
# if a > b:
#     print('a is biger than b')
# elif a < b:
#     print('a is smaller than b')
# else:
#     print('No match found')




# a = 'i love bangladesh'

# print('b' not in a)
# if 'b' in a:
#     print('Yes I found b')
# else:
#     print('I could not found b')


# a = 16

# if a > 10:
#     if a >= 20:
#         print('Above 10')
#     elif a <= 15:
#         print('Below 20')
#     else:
#         print('No Mactch Found.')
# else:
#     print('a is below 10')

# a = 'i love bangladesh'

# b = 'Yes I found "g"' if 't' in a else 'Not Found'

# print(b)
a = 20

# print(a < 22)

while a <= 10:
    print(a)
    a += 1
    a = a + 1

# while a <= 22:
#     print(a)
#     a += 1
# x = []
# while True:
    
#     print('Press A or a for Addition')
#     print('Press B or b for Subtruction')
#     print('Press C or c for Multiplcation')
#     print('Press E or e for Exit')
#     operators = input('Enter A Operatior : ').lower()
#     if operators == 'a' or operators == 'b' or operators == 'c' or operators == 'd':
#         if operators == 'a':
#             num1 = int(input('Enter First Number :'))
#             num2 = int(input('Enter Second Number :'))
#             print('==============================')
#             print(f"Result : {num1} + {num2} = {num1 + num2}")
#             x.append(num1 + num2)
#             print('==============================')
#         elif operators == 'b':
#             num1 = int(input('Enter First Number :'))
#             num2 = int(input('Enter Second Number :'))
#             print('==============================')
#             print(f"Result : {num1} - {num2} = {num1 - num2}")
#             x.append(num1 - num2)
#             print('==============================')
#         elif operators == 'e':
#             break
#     else:
#         print('==============================')
#         print('Invalid Input Try Again')
#         print('==============================')

#     print(x)


# a = 0
# while a < 10:
#     a += 1
#     if a == 3 or a == 4:
#         continue
#     print(a)
# else:
#     print('My While loop has been Done.')

# a = 'I Love Bangladesh'

# for i in a:
#     print(i)

# for i in range(11):
#     print(i)
# print(len(a))
# for i in range(len(a)):
#     if i == 5:
#         continue
#     print(i,a[i])

# x =0
# a = int(input('Enter A Number :'))

# while x < 10:
#     x +=1
#     print(f'{x} X {a} = {x * a}')

# for x in range(1,11):
#     print(f'{a} X {x} = {x * a}')

# x = 30

# a = f'My {x} age is dfg'
# print(a.format(x))

# print(a)
# a = 'I Love Bangladesh'

# for i in range(1,11):
#     print(i, end=' ')

# a = [10,'Banglaldesh',12.34,True]

# print(a[1:3])
# for i in a:
#     print(i, end=' ')

# print('Banglaldesh' in a)

# a.append('India')
# a.insert(1,'India')
# print(a.index(12.34))
# a.remove(True)
# print(a)
# b = []
# for i in a:
#     # if type(i) == bool:
#     #     a.remove(i)
#     # print(type(i))
#     if not isinstance(i,bool):
#         b.append(i)
# print(b)

# a = [10,'Banglaldesh',12.34,True,12.34]
# a = ['apple','Orange','Banana']
# a.remove(12.34)
# a.pop(1)
# print(a.count(12.34))
# print(a.index(12.34))
# a.reverse()
# a.sort()
# print(a)
# b = []
# for index, i in enumerate(a):
#     if i == 12.34:
#         b.append(index)

# print(b)
# print(enumerate(a))

# b = []

# for i in range(len(a)):
#     if a[i] == 12.34:
#         b.append(i)

# print(b)

# a.clear()
# print(a)

# b = a.copy()
# b.remove(True)
# print(b)
# print(a)

# b = [1,2,4,5,6]
# # a.extend(b)
# # print(a)
# for i in b:
#     print(i)
    # a.append(i)
# print(a)

# a = (10,'Banglaldesh',12.34,True,12.34)
# print(a)
# # print(a.index(12.34))

# b = list(a)
# b.remove('Banglaldesh')
# # print(b)
# a = tuple(b)
# print(a)

# a = {'name':'Rahim', 'age': 34,'country':'Bangladesh'}

# print(a['name'])
# print(a['age'])
# for i in a.keys():
#     print(i)

# for i,j in a.items():
#     print(i,j)

# b = a.copy()
# # b.update({'city':'Dhaka'})
# b.popitem()
# print(b)
# a = {'Dhaka','Rajshahi', 'Khulna', 'Jeshor'}
# b = {'Dhaka','Mymensing','khulna','Jeshor'}

# print(a)

# for i in a:
#     print(i)
# a.add(12)
# b = a.copy()
# a.update(b)

# b.difference_update(a)
# a.discard('3434')
# a.pop()
# a.remove('3434')
# c = a.intersection(b)
# a.intersection_update(b)
# c = a.union()
# print(c)

# a |= b
# print(a)

# def myfun():
#     for i in range(10):
#         print('I Love Bangladesh') 


# for i in range(11):
#     print(i)

# myfun()

# print(*range(1,10))

# a = [1,2,3,4,5,6]

# print(*a)

# def myfun():
#     for i in range(10):
#         print('I Love Bangladesh') 


# def my_fun(*name):
#     # print(f'My Name is {name[0]}')
#     return f'My Name is {name}'

# print(my_fun('Rahim'))

# def my_func(num1,num2):
#     print(f'Result {num1} + {num2} = {num1+num2}')

# a = float(input('Enter A Number: '))
# b = float(input('Enter A Number: '))
# my_func(123,34,6)


# def my_func(a):
#     if a == 0 or a == 1:
#         return 1
#     return a * my_func(a -1)
    
# print(my_func(5))


# def myfun(a):
#     # print(a)
#     return a

# print(myfun(12))

# def my_fun(a):
#     if len(a) == 0:
#         return ""
#     return a[-1] + my_fun((a[:-1]))

# print(my_fun('Bangladesh'))

# a = 'Bangladesh'

# print(a[:-1])

# a = lambda num1, num2: num1 + num2
# print(a(12,67))

# a = 20

# b = 40

# if a > b:
#     c = a - b
# else:
#     c = b - a
# c = a - b if a > b else b - a
# print(c)

# a = []

# for i in range(1,10,2):
#     a.append(i)

# print(a)
# a = []
# a = [i for i in range(1,10)]
# print(a)

# a = lambda num1, num2: num1 + num2
# print(a(12,67))

# def a(num1,num2):
#     return num1 + num2

# print(a(12,34))

# a = lambda num1,num2: num1 + num2

# print(a(12,34))


# a = open('E:\\Universal IT\\Batch - 106\\newfile.txt','r')
# a = open('newfile.txt','r')

# print(a)

# print(a.read())
# print(a.read(10))
# print(a.readlines()[3])
# print(a.readline())
# print(a.readline())
# b = []
# a = open('newfile.txt','w')
# a = open('Mustak.txt','a')
# a.write('We Are Learning Ml File Handaling.')
# a.close()
# a = open('newfile.txt','r')
# print(a.read())

# a = open('Mustak.txt','r')
# print(a.read())

# try:
#     a = open('Mustak.txt','r')
#     print(a.read())
# except :
#     print('File Not Found Amamr Shonar Bangla')

# while True:

#     a = input('Enter A Number : ')
#     b = int(input('Enter A Number : '))

#     try:
#         print(a + b)
#     except Exception as e:
#         print(e)

# try:
#     print(a + b)
# except:
#     print('Format Not Match')

# a = open('newfile.txt','r')

# print(a)

# print(a.read(22))
# from my_module import my_fun
# import my_module


# import my_module

# a = float(input('Enter A Number : '))
# b = float(input('Enter A Number : '))

# my_fun(a,b)
# my_var = 10
# my_var_2 = 20

# my_list = [12,34,45,45]

# def my_fun(num1,num2):
#     print(num1 + num2)

# from datetime import datetime

# a = datetime.now()

# print(a)


# import turtle

# a = turtle.Screen()
# a.bgcolor('white')
# a.title('Amar Shonar Bangla')

# b = turtle.Turtle()
# b.shape('classic')
# b.color('blue')
# b.speed(1)

# for i in range(4):
#     b.forward(100)
#     b.left(90)

# my_turtle.penup()
# my_turtle.goto(-150,100)
# my_turtle.pendown()

# my_turtle.color('green')
# my_turtle.circle(50)

# screen.mainloop()

# from datetime import datetime, timezone

# a = datetime.now()
# # a = datetime.utcnow()
# c = datetime.now(timezone.utc)
# b = a.strftime('%Y-%m-%d %I:%M:%S')

# # print(a)
# # print(b)
# print(c)

# import os

# os.mkdir('My Folder')

# from My_Folder import my_module
# a = 12

# class myclass:
#     a = 10
#     # a = 12
#     b = 20
    
#     def addition(self,num1=None,num2=None):
#         # if num1 is not None:
#         #     num1
#         # else:
#         #     self.a

#         num1 = num1 if num1 is not None else self.a
#         num2 = num2 if num2 is not None else self.b
#         print(num1 + num2)
        

#     c = [2,4,8,9]

# x = myclass()

# myclass()

# print(x.a)
# x.addition()

# class myclass:
#     z = 10
#     def __init__(self, a, b):
#         print(a + b)


# a = myclass(4,4)

# print(a)
# print(a.gggg)

# class A:
#     a = 10
#     b = 20
    
# class C:
#     z = 34

# class B(A,C):
#     c = 30
#     d = 40

# x = B()

# print(x)

# class car:
#     # def __init__(self,brand, model):
#     #     self.brand = brand
#     #     self.model = model

#     def move(self):
#         return('Drive')

# class Plane:
#     # def __init__(self,brand, model):
#     #     self.brand = brand
#     #     self.model = model

#     def move(self):
#         return('Fly')

# class Boat:
#     # def __init__(self,brand, model):
#     #     self.brand = brand
#     #     self.model = model

#     def move(self):
#         return('Sail')

# a = car()
# b = Plane()
# c = Boat()


# # z = [a,b,c]
# z = [car(),Plane(),Boat()]

# for i in z:
#     print(i.move())


# students = []

# while True:
#     print('\nEnter Students Information :')
#     print('\n If Any One Press E or e instade of Name Then Program will be Exit.')
#     name =input('Enter Name : ')
#     if name.lower() == 'e':
#         break

#     roll =input('Enter Roll : ')

#     student = {
#         'name' : name,
#         'roll' : roll
#     }

#     students.append(student)

# print('\nFinal List Of the Students')

# for student in students:
#     print(student)

# students = {}

# while True:
#     key = input('Enter Name :')

#     if key.lower() == 'e':
#         break
    
#     value = input(f'Enter Value For {key} :')
#     students[key] = value

# print(students)

# while True:
#     name = input('Enter Name :')

#     if name.lower() == 'e':
#         break
    
#     roll = input('Enter Roll : ')
#     students['name'] = name
#     students['roll'] = roll

# print(students)
    
    