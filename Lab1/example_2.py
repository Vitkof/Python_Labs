
def input_data():
    f = open('number.txt', 'r')
    nums_str = f.read().split()
    f.close()
    nums = [int(el) for el in nums_str]
    print("Input:   " + format(nums))
    return nums


# Quick Sort. быстрая сортировка. Сложность N * log N
def separator(arr, low, high):
    pivot = arr[(low + high) // 2]  # опорный - средний элемент
    x = low   # low - нижняя граница
    y = high   # high - верхняя граница
    while True:
        while arr[x] < pivot:
            x += 1

        while arr[y] > pivot:
            y -= 1

        if x >= y:  # Обмен происходит до тех пор, пока индексы не пересекутся.
            return y  # Алгоритм возвращает последний индекс
        arr[x], arr[y] = arr[y], arr[x]


def quick_sort(arr):
    # Создадим рекурсивную функцию, вызывающую себя, пока не 1 элемент
    def recursion_quick_sort(array, low, high):
        if low < high:
            sep_index = separator(array, low, high)
            recursion_quick_sort(array, low, sep_index - 1)
            recursion_quick_sort(array, sep_index + 1, high)
    recursion_quick_sort(arr, 0, len(arr) - 1)
    return arr


# Merge_Sort. сортировка слиянием. Сложность N * log N
def merge(arr1, arr2):
    res_arr = []

    # Сравниваем первые элементы в начале каждого списка
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            res_arr.append(arr1[0])
            del arr1[0]

        else:
            res_arr.append(arr2[0])
            del arr2[0]

    # выход из while означает, что достигнут конец какого-то массива.
    # Если в 1м еще остались, добавляем их в конец отсортированного
    if len(arr1) > 0:
        [res_arr.append(el) for el in arr1]
    # Если же во 2-м, то добавляем их
    if len(arr2) > 0:
        [res_arr.append(el) for el in arr2]

    return res_arr


def merge_sort(arr):
    # Если состоит из 1 элемента, - возврат
    if len(arr) < 2:
        return arr
    # Сортируем левую/правую половину
    else:
        sred = len(arr) // 2
        left_half = merge_sort(arr[0: sred])  # левосторонняя рекурсия
        right_half = merge_sort(arr[sred:])  # правосторонняя рекурсия

    # делаем слияние половин в единый отсортированный
    return merge(left_half, right_half)


# Radix LSD sort. Поразрядная. Сложность k(N+10), k- количество цифр(разрядность).   О(n).
def radix_sort(arr):
    # Находим наибольшее число, чтоб определить разрядность
    biggest_number = max(arr)
    max_razr = 0
    while biggest_number != 0:
        biggest_number //= 10
        max_razr += 1

    # Проходим по разрядам справа-налево, т.к. у нас LSD-сортировка
    for r in range(max_razr):
        heaps_list = [[] for cifr in range(10)]      # список кучек [] для каждой цифры разряда
        for el in arr:
            ch = el // (10 ** r) % 10
            heaps_list[ch].append(el)

        arr = []
        for cifra in range(10):
            arr += heaps_list[cifra]
        print("Sorted by {} razryad: ".format(r), arr)

    return arr


print("Quick Sort: {}\n".format(quick_sort(input_data())))
print("Merge Sort: {}\n".format(merge_sort(input_data())))
print("Radix LSD sort: {}".format(radix_sort(input_data())))
