
# coding: utf-8

# In[ ]:


'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: 
они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, 
т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. 
Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, 
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. 
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Есть вопросы по задаче? Запроси помощь ассистента: https://welcome.stepik.org/ru/assistant
'''
def ende_code(s, encode, a_from, a_to):
    code = dict()

    if encode:
        tmp = a_from
        a_from = a_to
        a_to = tmp

    for i in range(len(a_from)):
        code[a_from[i]] = a_to[i]

    result = ''

    for c in s:
        result += code[c]

    return result

or_alf = input()
co_alf = input()

or_str = input()
co_str = input()

print(ende_code(or_str, False, or_alf, co_alf))
print(ende_code(co_str, True, or_alf, co_alf))
