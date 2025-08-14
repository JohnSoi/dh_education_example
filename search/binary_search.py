def binary_search(digit_list: list[int], need_digit: int) -> tuple[int | None, int]:
    """
    Бинарный поиск по списку. Если значения нет -None

    :param digit_list: список чисел для поиска
    :type digit_list: list[int]
    :param need_digit: искомое число
    :type need_digit: int
    :return: индекс элемента (None - если нет) и количество итераций
    :rtype: tuple[int | None, int]
    """
    iteration: int = 0
    low: int = 0
    high: int = len(digit_list)

    while low <= high:
        iteration = iteration + 1
        # каждый раз берем элемент из середины (по сути индекс)
        # это разделит список на 2 части
        middle: int = (low + high) // 2
        # значение среднего элемента
        guess: int = digit_list[middle]

        # число найдено
        if guess == need_digit:
            return middle, iteration

        # Если искомое число меньше - то мы уменьшаем границу влево
        # (то есть берем левую часть нашей половинки списка).
        # Иначе - уменьшаем границу вправо (берем правую или большую часть)
        if need_digit < guess:
            high = middle - 1
        else:
            low = middle + 1

    return None, iteration


example_digit_list: list[int] = list(range(0, 1000))


if __name__ == '__main__':
    print(binary_search(example_digit_list, 999)) # Индекс - 999, итераций - 9
    print(binary_search(example_digit_list, 0)) # Индекс - 0, итераций -9
    print(binary_search(example_digit_list, 500)) # Индекс - 500, итераций - 1
    print(binary_search(example_digit_list, 750)) # Индекс - 750, итераций - 2