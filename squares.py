
# coding: utf-8

# In[ ]:


'''
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и 
соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:

треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности
'''
t = str(input())
if t == ('треугольник'):
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2 
    s = ((p*(p-a)*(p-b)*(p-c))**0.5)
    print(s)
elif t == ('прямоугольник'):
    a = float(input())
    b = float(input())
    s = a * b
    print(s)
elif t == ('круг'):
    r = float(input())
    s= 3.14 * r * r
    print(s)

