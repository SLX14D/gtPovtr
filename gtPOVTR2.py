#Задание 1
# def square(x):
#     """
#     Возвращает квадрат числа.

#     Примеры:
#     >>> square(2)
#     4
#     >>> square(-3)
#     9
#     >>> square(0)
#     0
#     """
#     return x * x


# if __name__ == "__gtPOVTR2__":
#     import doctest
#     doctest.testmod()

# #Задание 2
# import logging

# logging.basicConfig(level=logging.INFO)

# def greet(name):
#     logging.info(f"Вызваана функция greet с аргументом {name}")
#     print(f"Hello, {name}!")
# greet("Alice")

#Задание 3
# def safe_div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Деление на 0!!!!!")
#         return None
# print(safe_div(10, 2)) 
# print(safe_div(5, 0)) 

#Задание 4
def repeat(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat
def hello():
    print("Hello!")
hello()
