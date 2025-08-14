from simple_search import simple_search
from binary_search import binary_search


if __name__ == '__main__':
    example_list_1: list[int] = list(range(101))
    example_list_2: list[int] = list(range(10_001))
    example_list_3: list[int] = list(range(100_000_001))

    _, simple_iteration_1 = simple_search(example_list_1, 100)
    _, binary_iteration_1 = binary_search(example_list_1, 100)

    print(f"Количество итераций простого поиск из 99 элементов: {simple_iteration_1}") # 101
    print(f"Количество итераций бинарного поиск из 99 элементов: {binary_iteration_1}") # 6
    print(f"Бинарный быстрее на: {100 - binary_iteration_1 * 100 / simple_iteration_1:.2f} %") # 94.06%

    _, simple_iteration_2 = simple_search(example_list_2, 10_000)
    _, binary_iteration_2 = binary_search(example_list_2, 10_000)

    print(f"Количество итераций простого поиск из 10 000 элементов: {simple_iteration_2}") # 10 001
    print(f"Количество итераций бинарного поиск из 10 000 элементов: {binary_iteration_2}") # 13
    print(f"Бинарный быстрее на: {100 - binary_iteration_2 * 100 / simple_iteration_2:.2f} %") # 99.87%

    _, simple_iteration_3 = simple_search(example_list_3, 100_000_000)
    _, binary_iteration_3 = binary_search(example_list_3, 100_000_000)

    print(f"Количество итераций простого поиск из 100 000 000 элементов: {simple_iteration_3}") # 100 000 001
    print(f"Количество итераций бинарного поиск из 100 000 000 элементов: {binary_iteration_3}") # 26
    print(f"Бинарный быстрее на: {100 - binary_iteration_3 * 100 / simple_iteration_3} %") # 99.999974 %

    _, simple_iteration_4 = simple_search(example_list_3, 0)
    _, binary_iteration_4 = binary_search(example_list_3, 0)

    print(f"Количество итераций простого поиск из 100 000 000 элементов: {simple_iteration_4}")  # 1
    print(f"Количество итераций бинарного поиск из 100 000 000 элементов: {binary_iteration_4}")  # 26
    print(f"Бинарный быстрее на: {100 - binary_iteration_4 * 100 / simple_iteration_4} %")  # -2500 %
