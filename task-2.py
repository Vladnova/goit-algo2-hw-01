import random

def quick_select(arr, k):
    # Перевірка валідності вхідних даних
    if k < 1 or k > len(arr):
        raise ValueError("k має бути у межах від 1 до довжини масиву")

    # Внутрішня функція Quick Select
    def quick_select_recursive(arr, left, right, k_index):
        # Вибір опорного елемента
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]

        # Перестановка опорного елемента в кінець
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        # Розподіл елементів відносно pivot
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        # Переміщення опорного елемента у свою позицію
        arr[store_index], arr[right] = arr[right], arr[store_index]

        # Якщо опорний елемент - це k-й найменший елемент
        if store_index == k_index:
            return arr[store_index]
        # Якщо k-й елемент знаходиться ліворуч
        elif store_index > k_index:
            return quick_select_recursive(arr, left, store_index - 1, k_index)
        # Якщо k-й елемент знаходиться праворуч
        else:
            return quick_select_recursive(arr, store_index + 1, right, k_index)

    # Індекс k-го найменшого елемента (0-based)
    k_index = k - 1
    return quick_select_recursive(arr, 0, len(arr) - 1, k_index)

# Приклад використання
array = [21, 13, 4, 9, 15, 7]
k = 3
result = quick_select(array, k)
print(f"{k}-й найменший елемент: {result}")
