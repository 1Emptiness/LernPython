""" 
print("hello", 5.5, 4, sep=", ", end="!" "\n")
print("\t", "hello, 5.5, 4!")
print('Dan\'s book')
print('you / Book /')

#Mathematicks

print(-7+3.4/2)
print(2**4)

print("Мин число", min(5, 2, 6, 1),"\n","Макс число", max(4, 6, 2), "\n", "Число по модулю", abs(-3), "\n", "Округляем число", round(7.4243), round(9.678))
print("привет")
print('різдво')
print(20.6 % 2)

print("Введите число для вывода input: ")

print("Следующий урок!")
a = 6
second = 4
print("Додаем два числа", a + second) """


""" for i in range(5, 16, 3):
    print(i) 


print('\n\n')

word = 'Some text'
for i in word:
    if i =='m':
        print('Літера m є у тексті')
    print(i) """


""" work = True

while work:
    user_input = input('Enter wird STOP: ')
    if user_input == "STOP":
        work = False

print('While loop is done')   """


# Операторы в цмклах

""" for i in range(1, 11):

    if i % 2 != 0:
        continue

    if i ==8:
        break
    print("El: ", i) """


""" for i in "Hello world":
    if i == 'w':
        print('Done')
        break
else:
    print('Not faund') """

# Списки данных

""" a = 3
b = a + 3

nums = [5, 7, 5.23, -4, -222, 2334]

nums[0] = 34.22

print(nums[3])



nums2 = [24]
print(nums2[-1][0])


nums.append(45)
nums.insert(1, False,) #False = 0, True = 1
nums.extend([nums2])
nums.sort()
nums.reverse()# перевернуть сортировку
nums.pop()# удалить последний элемент списка
nums.remove(2334)# удаляет элемент по значению
nums.clear()# очищает список

print(nums)
print(nums.count(-4))# Ищет количество по значению

print(len(nums))# длина списка """

# списки и циклы

""" nums = [5, 3, 2, 0, 34, 43, 4, 34]

for i in nums:
    res = nums[0]
    res = res ** 2
    print(res) """

""" user_count_nobby = int(input('Enter hobby number: '))

i = 0

hobby = []

while i < user_count_nobby:
    text = "Enter hobby: " + str(i + 1) + ": "
    hobby.append(input(text))

    i += 1

print(hobby) """




""" a = [2, 5, 6, 10, 13, 17, 20]

for i in a:
    if i % a[0] == 0:  # Проверка делимости текущего элемента на первый элемент
        print(i)
 """


""" a = [1, 2, 3, 5, 3, 8]
d1, d2, d3 = a


print(d3) """


""" #задание 1

# Создаем список строк
name_line = ['Dan', 'San', 'Bon', 'Like']

# Добавляем элемент 'Silver' в конец списка
name_line.append('Silver')
name_line.append('York')
name_line.remove('York')

# Проверяем результат
print(name_line)
 """



""" #задание 2
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]


print(mat)


# вывод строк
print("mat[0]: ", mat[0])
print("mat[1]: ", mat[1])
print("mat[2]: ", mat[2])

# вывод элементов по отдельности
print("mat[0][0]: ", mat[0][0])
print("mat[0][1]: ", mat[0][1])
print("mat[0][2]: ", mat[0][2])
print("mat[1][0]: ", mat[1][0])
print("mat[1][1]: ", mat[1][1])
print("mat[1][2]: ", mat[1][2])
print("mat[2][0]: ", mat[2][0])
print("mat[2][1]: ", mat[2][1])
print("mat[2][2]: ", mat[2][2])
 """

""" #задание 3
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# вывод матрицы с помощью цикла
for i in range(3):
    for j in range(3):
        print(mat[i][j], end = " ")
    print() # перевод на другую строку
 """
#задание 4
""" line_str = [10, 20, 10, 20, 30, 40, 30, 50]

# Новый список для хранения уникальных элементов
unique_name_line = []

# Проходим по каждому элементу оригинального списка
for name in line_str:
    # Если элемент еще не в новом списке, добавляем его
    if name not in unique_name_line:
        unique_name_line.append(name)

# Проверяем результат
print ("Начальный список: ", line_str)

print ("После удаления дублей: ", unique_name_line)

 """
""" #задание 5
# списки чисел
numbers = []
squares = []
cubes = []
# начальное и конечное значения диапазона
start = 1
end = 10
# цикл добавления чисел в список
for count in range (start, end+1) :
    numbers.append (count)
    squares.append (count**2)
    cubes.append (count**3)
 
 
print ("numbers: ",numbers)
print ("squares: ",squares)
print ("cubes : ",cubes) """



""" line_nach = [10, 20, 30, 40, 50]

print(line_nach)

un_line = line_nach

un_line.sort(reverse=True)

print(un_line) """


""" line_god = [11, 22, 33, 44, 55]


for i in line_god:
    if(i%2 == 0):
        line_god.remove(i)

print ("Список с нечетными числами: ", line_god) """

""" import itertools

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30]

# Используем zip_longest с fillvalue=0 для дополнения более короткого списка нулями
result = [x + y for x, y in itertools.zip_longest(list1, list2, fillvalue=0)]

print(result)  # Output: [11, 22, 33, 4]


#066 360 0946

def dot(v1, v2):
    # Инициализируем переменную для хранения результата скалярного произведения
    c = 0
    
    # Используем функцию zip для одновременной итерации по обоим спискам
    for n, m in zip(v1, v2):
        # Умножаем соответствующие элементы списков и добавляем результат к переменной c
        c = c + n * m
        
    # Возвращаем результат скалярного произведения
    return c
 
# Создаем первый список (вектор)
list1 = [1, 2, 3, 4]

# Создаем второй список (вектор)
list2 = [5, 6, 7, 8]

# Вызываем функцию dot для вычисления скалярного произведения list1 и list2
result = dot(list1, list2)
 
# Печатаем первый вектор
print("Первый вектор: ", list1)

# Печатаем второй вектор
print("Второй вектор: ", list2)

# Печатаем результат скалярного произведения
print("Скалярное произведение: ", result)
 """


""" 
# Создаем список чисел
num_list = [1, 2, 3, 7, 10, 15]

# Добавляем 5 к каждому элементу списка
num_list = [x + 5 for x in num_list]

# Удаляем все числа, которые больше 10
num_list = [x for x in num_list if x <= 10]

# Проверяем результат
print(num_list)

 """

""" list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = [x for x in list1 if x in list2]

llist3 = list1 + list2

list4 = []

for name in llist3:
    if name not in list4:
        list4.append(name)

print ("Список: ", list4) """

""" 
def unique_elements(list1, list2):
    # Создаем множества из исходных списков, чтобы удалить дубликаты
    set1 = set(list1)
    set2 = set(list2)
    
    # Объединяем множества, чтобы получить уникальные элементы из обоих списков
    unique_items = set1.union(set2)
    
    # Преобразуем множество обратно в список (если нужно)
    unique_list = list(unique_items)
    
    return unique_list

# Создаем первый список (вектор)
list1 = [1, 2, 3, 4]

# Создаем второй список (вектор)
list2 = [5, 6, 3, 8]

# Получаем список c уникальными элементами из обоих списков
unique_elements_list = unique_elements(list1, list2)

print("Уникальные элементы из обоих списков:", unique_elements_list) """

""" 
a = int(input('Введите свой возраст: '))

if a <18:
    print('Ваш возраст не потходит для этого сайта')

else:
    print('Удачи')
 """

# Запрос даты рождения
a = int(input('Введите свой день рождения (число): '))
b = input('Введите свой месяц рождения (на русском языке): ')
c = int(input('Введите свой год рождения: '))

# Проверка корректности введенных данных
# Проверяем день (допустим, все месяцы имеют 31 день для простоты)
if not (1 <= a <= 31):
    print('Вы ввели не существующую дату')

# Проверка месяца (допускаем все русские названия месяцев)
elif b not in ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']:
    print('Вы ввели не существующий месяц')

# Проверка года (условно считаем, что год должен быть после 2005)
elif c > 2005:
    print('Ваш возраст не подходит')

else:
    # Вывод введенных данных
    w = [a, b, c]
    print('Ваш лист: ', w)

    print('Вот ваши данные: ')
    print('Ваш день рождения:', a)
    print('Ваш месяц рождения:', b)
    print('Ваш год рождения:', c)

