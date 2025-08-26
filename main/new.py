# print(9**19 - int(float(9**19)))
import math

#name = input('Enter your name:')
# print('Hello,', name)

# a = True
# b = False
# print(a and b or not a and not b)

# a = 'string'
# b = 'another string'
# print(a + '\n' + b)

# print("123" + "42")
# print('a' * 3)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)

# a = [1, 2, 3]
# b = a
# print('# значения списка b?', b)

# a[1] = 10
# print('# значения списка b?', b)
#
# b[0] = 20
# print('# значения списка a?', a)
#
# a = [5, 6]
# print('# значения списка b?', b)

# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))

# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))

# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)


# def h():
#     print("- H")
#     print("- 12")
#     print("H - end")
#
# def f():
#     print("- F")
#     g(h)
#     print("F - end")
#
# def g(a):
#     print("- G - ",a)
#     a()
#     print("G - end")
#
# print("\nMODULE")
# g(f)

print(str(math.ceil(math.pow(math.pi, math.e)*10000)))