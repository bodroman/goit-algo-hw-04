import timeit
import random

# Реалізуємо алгоритми сортування

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort (вбудована функція Python)
def timsort(arr):
    arr.sort()

# Використаємо функцію для тестування часу виконання
def test_sorting_algorithm(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Основна частина коду виглядає так
sizes = [100, 1000, 5000, 10000]

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    
    # Тестування Merge Sort
    data_copy = data.copy()
    time_merge_sort = test_sorting_algorithm(merge_sort, data_copy)
    print(f"Merge Sort ({size} elements): {time_merge_sort:.6f} seconds")

    # Тестування Insertion Sort
    data_copy = data.copy()
    time_insertion_sort = test_sorting_algorithm(insertion_sort, data_copy)
    print(f"Insertion Sort ({size} elements): {time_insertion_sort:.6f} seconds")

    # Тестування Timsort
    data_copy = data.copy()
    time_timsort = test_sorting_algorithm(timsort, data_copy)
    print(f"Timsort ({size} elements): {time_timsort:.6f} seconds")
