from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, iterator_numbers))  #  заменить на map и filter

    for num in range(10):  # напечатать первые 10 чисел
        print(next(numbers))  #  с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
