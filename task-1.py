def find_min_max(arr):
    # Базовий випадок: якщо масив містить лише один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Базовий випадок: якщо масив містить два елементи
    if len(arr) == 2:
        return min(arr), max(arr)

    # Розділення масиву на дві частини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])  # Мінімум і максимум у лівій половині
    right_min, right_max = find_min_max(arr[mid:])  # Мінімум і максимум у правій половині

    # Повернення глобального мінімуму і максимуму як кортеж
    return min(left_min, right_min), max(left_max, right_max)

# Приклад використання
array = [3, 1, 5, 9, 12, 5, 8, 43]
result = find_min_max(array)
print(f"(Мінімум, Максимум): {result}")
