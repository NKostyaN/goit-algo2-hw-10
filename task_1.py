import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


sizes = [10000, 50000, 100000, 500000]
res_randomized = []
res_deterministic = []

for size in sizes:
    rand_times = []
    det_times = []

    for _ in range(5):
        array = [random.randint(0, 1000000) for _ in range(size)]

        arr_copy = array.copy()
        start = time.time()
        randomized_quick_sort(arr_copy)
        end = time.time()
        rand_times.append(end - start)

        arr_copy = array.copy()
        start = time.time()
        deterministic_quick_sort(arr_copy)
        end = time.time()
        det_times.append(end - start)

    random_time = sum(rand_times) / len(rand_times)
    deterministic_time = sum(det_times) / len(det_times)

    res_randomized.append(random_time)
    res_deterministic.append(deterministic_time)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {random_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд\n")


plt.figure(figsize=(10, 6))
plt.plot(sizes, res_randomized, label="Рандомізований QuickSort")
plt.plot(sizes, res_deterministic, label="Детермінований QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
