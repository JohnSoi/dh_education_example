def simple_search(digit_list: list[int], need_digit: int) -> tuple[int | None, int]:
    """
    Простой поиск вхождения числа перебором. Если значения нет -None

    :param digit_list: список чисел для поиска
    :type digit_list: list[int]
    :param need_digit: искомое число
    :type need_digit: int
    :return: индекс элемента (None - если нет) и количество итераций
    :rtype: tuple[int | None, int]
    """
    iteration: int = 0

    for index, digit in enumerate(digit_list):
        iteration = iteration + 1

        if digit == need_digit:
            return index, iteration

    return None, iteration


example_digit_list: list[int] = list(range(0, 1000))


if __name__ == '__main__':
    print(simple_search(example_digit_list, 999)) # Индекс - 999, итераций - 1000
    print(simple_search(example_digit_list, 0)) # Индекс - 0, итераций - 1
