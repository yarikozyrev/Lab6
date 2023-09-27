counter1 = 0  # Вспомогательный счетчик
while counter1 != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        matrix_size = int(input('Введите числом размерность квадратичной матрицы: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        counter1 += 1
        counter1 = counter1
        print('Размерность вашей матрицы:', matrix_size, 'на', matrix_size)

matrix = [[0] * matrix_size for _ in range(matrix_size)]
# print(matrix)

header_matrix = []
counterheader = 1
for counter in range(matrix_size):  # Заполнение шапки таблицы горизонтально(основных критериев)
    print(counterheader, 'условие')
    row = input().split()
    for counter in range(len(row)):
        row[counter] = (row[counter])
        counterheader += 1
    header_matrix.append(row)
# print('    ', header_matrix, sep=' ')

# for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
# print(header_matrix[counter], sep='\n')

help1 = 0
help = 0
ss = []
k = 0
print('Таблица отношений: ')
print(
    '1 -равная важность\n3 -умеренное превосходство одного над другим\n5 -существенное превосходство одного над другим\n7 -значительное превосходство одного над другим\n9 -очень сильное превосходство одного над другим\n2, 4, 6, 8 -соответствующие промежуточные значения\n')
while k < 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        for counter2 in range(matrix_size):  # Заполняем матрицу
            if help1 != matrix_size:
                if help1 == 0:
                    help1 += 1
                    one = 1
                    ss.append(one)
                else:
                    print('Введите ваше отношение в числовом эквиваленте', header_matrix[0], 'на', header_matrix[help1])
                    answer = int(input())
                    ss.append(answer)
                    help1 += 1
    except ValueError:
        print('Вы ввели не число!\nПопробуйте снова\n')
    else:
        k += 1

matrix[0] = []
matrix[0].append(ss)
dd = []
helpzero = 0
helpone = 1

counteritem = 1  # Вспомогательный счетчик
for item in ss:  # Заполняет весь первый столбик
    if counteritem == len(ss):
        break
    s2 = 1 / ss[helpone]
    sanswer = round(s2,2) #int(s2 * 100) / 100  # Два знака после запятой   #Переделал округление
    matrix[counteritem][0] = (sanswer)
    helpzero += 1
    helpone += 1
    counteritem += 1

dd = []
counteritem1 = 1  # Вспомогательный счетчик
for item1 in range(matrix_size):  # Заполняет единицы по диагонали
    if item1 != 0:
        matrix[item1][counteritem1] = 1
        counteritem1 += 1

# print('Матрица', *matrix, sep='\n')

leftobj = 0
helpobj = 1
subtractfirst = 2
helpcounter = matrix_size
helpmatrixsize = matrix_size
while helpcounter != 0:
    helpcounter = helpmatrixsize - subtractfirst  # Кол-во оставшихся элементов в строке, которые нужно ввести
    subtractfirst += 1  # Шаг вычитания
    leftobj += helpcounter  # Кол-во объектов, которые нужно ввести

print('Осталось ввести - ', leftobj, 'элементов')

u = 0
help1 = 0
helpobj = 1
helpone = 1

gorizont = 1
vertical = 2
spind = []
header_matrix = header_matrix

for i in range(matrix_size - 1):  # Узнаем индексы единичек, а после вводим дальше необходимые данные
    index = matrix[helpobj].index(helpone)
    spind.append(index)
    helpobj += 1

n = 0
element = 1
element2 = 2  # Сейчас заполняем правую диагональ матрицы
chetchik = 0
while chetchik != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода

    try:
        for j in range(1, matrix_size - 1):  # Работаем от (1:размера матрицы-1) строки
            for k in range(spind[n], matrix_size - 1):  # Работаем от (Индекса 1:размера матрицы-1) элементы в строке
                print('Введите ваше отношение в числовом эквиваленте', header_matrix[element], 'на',
                      header_matrix[element2])
                cntrlv = int(input())
                matrix[element][element2] = cntrlv
                element2 += 1
                if element2 + 1 > matrix_size:
                    element += 1
                    n += 1
                    element2 = 2 + n

                if n > len(spind):
                    break
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        chetchik += 1
# Заполнен 1 столбик, единицы, правая диагональ


counteritem_1 = 1  # Вспомогательный счетчик
step = matrix_size
helptwo = 2
numind = 0

for l in range(matrix_size - 2):  # Заполняем левую диагональ столбцами, кроме первого
    spisok = []
    # print('L', l)
    helpzero = 0
    hcounter = 2 + l
    num = 1 + l
    nhelp = 2 + l
    numstroki = 1 + l
    zero = 0
    stopflag = int(matrix_size) - 2
    if numstroki == matrix_size:
        break
    for i in matrix[numstroki]:  # Составили список элементов после 1
        if zero == stopflag:
            break
        if nhelp >= matrix_size:
            break
        a = matrix[numstroki][nhelp]
        spisok.append(a)
        nhelp += 1
        zero += 1
        # print('spisok', spisok)

    for h in spisok:
        if num == matrix_size:
            break
        a2 = 1 / spisok[helpzero]
        aanswer = round(a2,2)   #int(a2 * 100) / 100    #Переделал округление
        matrix[hcounter][num] = aanswer
        helpzero += 1
        hcounter += 1

print('    ', header_matrix)

for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
    print(header_matrix[counter], ' | ', matrix[counter], sep=' ')  # Не получается у меня вывести человеческую таблицу

sss = []
spissr = []
summa_vsego = 0
for o in range(matrix_size):        #Сумма строк
    if o == 0:
        mhelp = ss
    else:
        mhelp = matrix[o]

    sumOfElements = sum(mhelp)
    #srznach = sumOfElements / len(matrix[o])
    sranswer = round(sumOfElements,2)   #int(sumOfElements * 100) / 100  # Два знака после запятой  #Переделал округление
    summa_vsego +=sranswer
    spissr.append(sranswer)

summa_vsegoclear = round(summa_vsego,2) #int(summa_vsego * 100) / 100   #Переделал округление

#print(sss,summa_vsegoclear)

ssshelp1 = []
sssschet = 0
for counter_1 in range(matrix_size):        #Оценка альернатив/функция полезности
    shelp = spissr[sssschet]
    ssshelp = (shelp) / (summa_vsegoclear)
    #print(ssshelp)
    helpclear = round(ssshelp,2)        #int(ssshelp * 100) / 100       #Переделал округление
    ssshelp1.append(helpclear)
    sssschet+=1


# Теперь будем смотреть равны ли все элементы оценки альтернатив 1 т.к, они должны быть равны 1
#print(ssshelp1)
sumssshelp1 = sum(ssshelp1) #Сумма всех оценок альтернатив
counter = 0
counter1 = 1
if sumssshelp1 !=1:
    if sumssshelp1 > 1:
        for i in range(len(ssshelp1)):
            summa_end = sum(ssshelp1)
            if summa_end == 1:
                break
            if ((ssshelp1[i] * 100 % 10) == 5) or (ssshelp1[i] * 100 % 100 % 10 == 5):
                zamena = ssshelp1[i] - 0.01
                ssshelp1[i] = zamena

    if sumssshelp1 < 1:
        for i in range(len(ssshelp1)):
            summa_end = sum(ssshelp1)
            if summa_end == 1:
                break
            if ((ssshelp1[i] * 100 % 10) == 5) or (ssshelp1[i] * 100 % 100 % 10 == 5):
                zamena = ssshelp1[i] + 0.01
                ssshelp1[i] = zamena


print('\nФункция полезности всех критериев!\n')
for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
    print(header_matrix[counter], ' | ', ssshelp1[counter], sep=' ')  # Не получается у меня вывести человеческую таблицу
