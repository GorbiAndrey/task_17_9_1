
#проверка корректности ввода последовательности
try:
    user_sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
except:
    print("Вы ввели не числовое значение")
    user_sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

#проверка корректности ввода числа
try:
    user_number = int(input("Введите число: "))
except:
    print("Вы ввели не числовое значение.")
    user_number = int(input("Введите число: "))

#функция сортировки
def sorted_list(list):
    sorted_list = sorted(list)
    return sorted_list

array = sorted_list(user_sequence)

#функция бинарного поиска числа в последовательности
def binary_search(array, element):
    mid = len(array) // 2
    low = 0
    high = len(array)-1

    while array[mid] != element and low <= high:
        if element > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value")
    else:
        print("ID = ", mid)

binary_search(array, user_number)
