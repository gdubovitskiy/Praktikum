'''
Напишите python-скрипт который посчитает среднее, медиану и моду для произвольной выборки.
Скрипт должен загружать данные из текстового файла с расширением .txt.
В текстовом файле находится произвольное количество (больше 10 и меньше 1000) целых положительных чисел,
записанных через пробел. Запрещается использовать любые сторонние библиотеки - чтение данных из файла и все расчеты должны
производиться посредством стандартных средств языка python.
'''


def median(lst: list):
    n = len(lst)
    index = len(lst) // 2
    if n < 1:
        return None
    if n % 2 != 0:
        return data[index] / 1.0
    else:
        return sum(data[index - 1:index + 1]) / 2.0


file_name = 'data_5.txt'
mean_data = 0
median_data = 0
mode_data = 0

try:
    with open(file_name) as f:
        data = list(map(int, f.read().split()))
        size_data = len(data)
except FileNotFoundError:
    print(f'File "{file_name}" not found. Please, move {file_name} to directory with .py program or run script from '
          f'directory with .py file.')
    exit(-1)
except ValueError:
    print(f'File "{file_name}" is not contain integer numbers. Check data of file.')
    exit(-1)

try:
    data.sort()
    mean_data = sum(data) / size_data
    median_data = median(data)
    mode_data = max(set(data), key=data.count)
except ZeroDivisionError:
    print(f'File "{file_name}" is empty!')
    exit(-1)

if size_data < 150:
    print('Data:', data)

print('Size of data:', size_data)
print('Mean value of data:', mean_data)
print('Median of data:', median_data)
print('Mode of data:', mode_data)