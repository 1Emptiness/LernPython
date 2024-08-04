import math

""" year = int(input("Введите число для определения: " ))
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Пример использования
if is_leap_year(year):
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.") """





""" print("Вас приветстувет програма для выполнения простых арифметических операций.\n"
      "Вы можете выполнить такие операции: +, -, *, /.")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
oper = input("Введите операцию: ")
def arithmetic(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Ошибка: деление на ноль!'
    else:
        return 'Ошибка: неверная операция'

result = arithmetic(num1, num2, oper)
print("Ваш ответ: ", result) """



""" print("Вас приветстувет програма для нахождения периметра квадрата, площади квадрата и диагонали квадрата.\n"
      "Все что вам нужно это ввести нужную сторону квадрата")


def square(storona):
    perimeter = storona * 4
    area = storona * 2
    diagonal = storona * math.sqrt(2)
    return (perimeter, area, diagonal)

# Запрашиваем у пользователя сторону квадрата
storona = float(input('Введите сторону квадрата: '))

# Вызываем функцию и получаем результаты
result = square(storona)

# Выводим результаты
print("Периметр: ", result[0])
print("Площадь: ", result[1])
print("Диагональ: ", result[2]) """


""" print("Вас приветстувет програма для нахождения времени года по месяцу.\n"
      "Все что вам нужно это ввести число месяца")

maunth = float(input('Введите число месяца: '))

def schet(maunth):
    if maunth <= 2:
        return('Зиме')
    elif maunth <=5 and maunth >=3:
        return('Весне')
    elif maunth <=8 and maunth >=6:
        return('Лету')
    elif maunth <=11 and maunth >=9:
        return('Осени')
    elif maunth == 12:
        return('Зиме')
    else:
        print('Введенны не верные даные, нужно ввести число от 1 до 12')

result = schet(maunth)

print('Этот месяц относиться к', result) """


""" print("Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых\n"
       "каждый год размер его вклада увеличивается на 10%.\n" 
       "Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).\n"
       "Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.\n")

a = float(input('Введите суму: '))
years = int(input('Введите количество лет: '))
annual_interest_rate = 10

final_amount = a
for _ in range(years):
    final_amount += final_amount * (annual_interest_rate / 100)

print(f"Итоговая сумма вклада через {years} лет: {final_amount:.2f} рублей")     """

""" print("Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,\n"
      "и возвращающую True, если оно простое, и False - иначе.\n")

a = int(input('Введите число для определения: '))

def is_prime(a):
    
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

result = is_prime(a)

print('Число ',result, 'простое') """


""" print("Написать функцию date, принимающую 3 аргумента — день, месяц и год.\n" 
      'Вернуть True, если такая дата есть в нашем календаре, и False иначе.')

day = int(input('Введите день: '))
month = input('Введите месяц: ')
year = int(input('Введите год: '))

def date(day, month, year):
    if date == day <=31:
        print(f"День {day} допустим.")
    else:
        print(f"День {day} недопустим.")
    
    if month in ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']:
        print(f"Месяц {month} допустим.")
    else:
        print(f"Месяц {month} недопустим.")
    
    
    if year > 0:
        print(f"Год {year} допустим.")
    else:
        print(f"Год {year} недопустим.")

result = date(day, month, year)
print("Ваша дата: ", result) """

""" def XOR_cipher(text, key):

    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(text)):
        encrypted_char = chr(ord(text[i]) ^ ord(key[i % key_length]))
        encrypted_text += encrypted_char
        
    return encrypted_text

def XOR_uncipher(encrypted_text, key):
   
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        decrypted_char = chr(ord(encrypted_text[i]) ^ ord(key[i % key_length]))
        decrypted_text += decrypted_char
        
    return decrypted_text

# Пример использования
text = input("Введите текст: ")
key = input("key")

# Шифрование
encrypted = XOR_cipher(text, key)
print(f"Зашифрованная строка: {encrypted}")

# Расшифрование
decrypted = XOR_uncipher(encrypted, key)
print(f"Расшифрованная строка: {decrypted}")
 """

""" import datetime

def date(day, month, year):
    try:
        # Пробуем создать объект даты с указанными параметрами
        datetime.date(year, month, day)
    except ValueError:
        # Если выброшено исключение ValueError, значит дата некорректна
        return False
    # Если исключение не выброшено, дата корректна
    return True

# Считываем данные от пользователя
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

# Проверяем корректность введенной даты
if date(day, month, year):
    print("Введенная дата корректна.")
else:
    print("Введенная дата некорректна.")
 """


""" word = list('stop')

word[0] = 'S'
word.append('!')
result = ''.join(word)
print(result) """

""" 
text = 'foodbol,baskedbol,skate'
hobies = text.split(',')

for i in range(0, len(hobies)):
    hobies[i] = hobies[i].capitalize() #верхний регистр в словах листа


result = ', '.join(hobies)
print(result)

 """


""" lis = [5, 3, True, 'phorever', 7, 13, 55]

print(lis[4:])

print(lis[2:-3])

print(lis[:3])

print(lis[2::2])

print(lis[::3])

print(lis[:-5:-1]) """
""" print('Введите любое число.')

a = int(input('Введите число наугад: '))

if a == 0:
    print("Вы наконецто ввели правильное число")
else:
    print('Введите правильное число!!!')

 """
""" 
def camel(st):
    result = []
    toggle = True  # Переключатель регистра

    for char in st:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if toggle:
                result.append(char.upper())
            else:
                result.append(char.lower())
            toggle = not toggle  # Переключаем регистр
        else:
            result.append(char)  # Добавляем символы без изменений

    return ''.join(result)

# Пример использования

print('Введите текст: ')
input_string = input(': ')
print("Вот ваш ответ:", camel(input_string))

 """

def shortener(st):
    result = []
    skip = 0  # Счетчик вложенности скобок

    for char in st:
        if char == '(':
            skip += 1  # Увеличиваем счетчик при открывающей скобке
        elif char == ')':
            skip -= 1  # Уменьшаем счетчик при закрывающей скобке
        elif skip == 0:
            result.append(char)  # Добавляем символ, если не внутри скобок

    return ''.join(result)

# Пример использования
input_string = "Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно."
print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))
print(shortener('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег'))


def cleaned_str(st):
    result = []
    
    for char in st:
        if char == '@':
            if result:
                result.pop()  # Удаляем последний символ из списка
        else:
            result.append(char)  # Добавляем символ в список
    
    return ''.join(result)

# Пример использования
input_string = "гр@оо@лк@оц@ва"
print(cleaned_str(input_string))  # Ожидаемый результат: "голова"

print(cleaned_str('сварка@@@@@лоб@ну@'))


inte = print('Sky')