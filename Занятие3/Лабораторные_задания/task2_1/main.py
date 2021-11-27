import json


def task() -> str:
    dict_numbers = {x: x**2 for x in range(1, 11)}  #  c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)  #  сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
