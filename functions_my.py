print('Функция 1: создает красивый резделитель из 10-и звездочек (**********)')

def simple_separator():
    x = '**********'
    return x
print(simple_separator())


print('Функция 2. создает разделитель из звездочек число которых можно регулировать параметром count')

def long_separator(count):
    sep = ''
    i = 1
    for i in range(count):
        sep += '*'
        i += 1
    return sep
count = int(input('Введите количество звёздочек для строки разделителя : '))
print (long_separator(count))


print('Функция 3. создает разделитель из любых символов любого количества')

def separator(simbol_mod, count):
    i = 1
    simbol = ''
    for i in range(count):
        simbol += simbol_mod
        i += 1
    return simbol
simbol = input('Введите символ, для разделителя')
count = int(input('Введите количество символов, для строки разделителя : '))
print(separator(simbol, count))


print('Функция 4. печатает Hello World в заданном формате\n')
def simple_separator():
    x = ' **********\n'
    return x
sep = simple_separator()

def simple2_separator():
    x = '##########\n'
    return x
sep2 = simple2_separator()

def hello_world():
    x = 'Hello World!\n'
    return x
print(simple_separator(), hello_world(), simple2_separator())


print('Функция 5. печатает приветствие в красивом формате')

def simple_separator():
    x = '**********\n'
    return x
sep = simple_separator()

def simple_separator2():
    x = '##########\n'
    return x
sep2 = simple_separator2()

def hello_who(name):
    x = 'Hello ' + name + '\n'
    return x
name = 'World!'
print('\n', sep, hello_who(name), sep2)

print('Функция 6. складывает любое количество цифр и возводит результат в степень power Версия №1 ')
def pow_many(power, *args):
    result = 0
    for number in args:
        result += number
    return result**power

print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


print('Функция 6. складывает любое количество цифр и возводит результат в степень power Версия №2 ')
def pow_many(numbers, power):
    sum = 0
    while numbers > 0:
        digit = numbers % 10
        sum = sum + digit
        numbers = numbers // 10
    return sum**power
numbers = int(input('Введите цифры, в любом количестве, для сложения : '))
power = int(input('Введите степень, для возведения суммы в неё : '))
print('Сумма введённых цифр ', numbers, ' возведённая в степень ', power, ' равняется = ', pow_many(numbers, power))


print('Функция 7 выводит переданные параметры в виде key --> value')

def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k, ' --> ', v)

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


print('Функция 8: лямбда-функции (без фильтрации через общую последовательность)')
"""
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит
    в новую последовательность  иначе нет (примеры ниже)
    :param iterable: входнaя последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
"""
iterable = [1, 2, 3, 4, 5]
iterable_2 = ['a', 'b', 'c', 'd']

a = lambda x: True if x > 3 else False
result = filter(a, iterable)
print('Новая последорвательность по условию >3: ', list(result))

a = lambda x: True if x == 2 else False
result = filter(a, iterable)
print('Новая последорвательность по условию =2: ', list(result))

a = lambda x: True if x != 3 else False
result = filter(a, iterable)
print('Новая последорвательность по условию !=3: ', list(result))

a = lambda x: True if x in 'abba' else False
result = filter(a, iterable_2)
print('Новая последорвательность по условию "abba" ', list(result))