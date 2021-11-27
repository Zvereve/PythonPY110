import json


def task():
    filename = "input.json"
    with open(filename, "r") as dat:# TOO считать содержимое JSON файла
        d = json.load(dat)
    gen_exr = map(lambda itm: itm["contains_improvement_appeals"],d)  # TO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
